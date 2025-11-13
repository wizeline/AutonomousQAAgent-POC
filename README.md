# AutonomousQAAgent-POC - GitHub Test Case Generator

This repository contains an n8n workflow that generates executable unit tests for repository source files using an LLM.

## Purpose

- Automatically generate production-ready unit tests for source files in a GitHub repository.
- Provide a repeatable workflow that can run in bulk (batch) or per-file (individual).

## Configuration parameters (what they do & where used)

All of these live in the `Configuration` node in the workflow (node name: `Configuration`). The node sets initial variables used across the flow.

- `owner` (string)

  - Description: GitHub repository owner/org (e.g., `wizeline`).
  - Where used: GitHub API requests to form repository URLs and fetch content.
  - Default in example: `wizeline`.

- `repo` (string)

  - Description: Repository name (e.g., `BytescribeTeam`).
  - Where used: GitHub API requests to fetch tree and file contents.
  - Default in example: `BytescribeTeam`.

- `branch` (string)

  - Description: Source branch to read files from (e.g., `main`).
  - Where used: API calls to read repository tree and file content.
  - Default in example: `main`.

- `processingMode` (string) — `batch` or `individual`

  - Description: Choose processing mode.
    - `batch`: groups multiple files into a single prompt (fewer AI calls, larger prompts).
    - `individual`: sends each file in its own prompt (more AI calls, more precise results per file).
  - Where used: `Route by Processing Mode` node to pick the route.
  - Default in example: `batch`.

- `batchSize` (number)

  - Description: Number of files included in each batch when `processingMode` is `batch`.
  - Where used: `Create Batches` node slices `sourceFiles` into groups of `batchSize`.
  - Effect: Controls prompt size and number of AI calls.
  - Example default in example: `5`.
  - Recommendation: 5–10 as a safe starting point (depends on token limits and file sizes).

- `fetchFileContent` (boolean)

  - Description: When `true` the workflow will fetch raw file content from GitHub (used for detailed generation or individual mode).
  - Where used: `Fetch File Content` and `Prepare Individual File` nodes.
  - Default in example: `true`.

- `maxFilesToProcess` (number)

  - Description: Maximum number of matching source files the workflow will process overall.
  - Where used: `Process File Structure` node uses `.slice(0, maxFilesToProcess)` when building the `sourceFiles` list.
  - Effect: Caps work done (useful for large repos and cost control).
  - Example default in example: `10`.

- `testBranch` (string)
  - Description: Branch name where auto-generated tests will be committed (e.g., `auto-generated-tests`).
  - Where used: Branch creation and commit nodes (`Prepare Branch Creation Data`, `Create Test Branch`, commit HTTP request).
  - Default in example: `auto-generated-tests`.

## Where parameters appear in the workflow

Key nodes (by name) and roles:

- `Process File Structure` (code node)

  - Reads the repository tree response and builds `sourceFiles` list (applies `maxFilesToProcess`).

- `Create Batches` (code node)

  - Uses `batchSize` to slice `sourceFiles` into batches (each batch becomes one prompt to the AI in batch mode).

- `Prepare Batch Prompt` (set node)

  - Builds the text prompt for a batch including a list of files.

- `AI - Batch Analysis` / `AI - Individual File Analysis` (language model nodes)

  - Send prompts and receive AI outputs.

- `Format Final Output` (code node)

  - Parses AI responses, aggregates test file metadata and contents, and returns a consolidated JSON structure.

- `Export to JSON File` (convertToFile node)

  - Writes the resulting JSON of generated tests to disk.

- `Prepare Git Commit` / `Create/Update File on GitHub` (code + httpRequest nodes)
  - Create/commit test files to the `testBranch` branch.

## Webhook Configuration
This webhook will listen for events from **GitHub Actions**. When the test results artifact is uploaded successfully, the webhook will be triggered to download the file and send "sample" files to a specific email address.

To set up the connection, you will configure your GitHub repository to use the n8n production webhook URL.

### Configuration Steps

1.  In your n8n workflow's Webhook node, copy the **Production URL** (or Test URL, depending on your environment).
2.  Open the **GitHub repository** where you want to register these webhook events.
3.  Click on the **"Settings"** tab of the repository.
4.  In the Repo Settings sidebar, click on **"Webhooks"**.
5.  Click the **"Add webhook"** button.
6.  In the "Payload URL" field, paste the link copied in **Step 1**.
7.  In the "Which events would you like to trigger this webhook?" section, tick the checkboxes for the following events:
    * **"Check runs"**
    * **"Pull requests"**
8.  Finally, ensure the "Active" box is ticked (it should be by default) and click **"Add webhook"** (or **"Update webhook"** if you are editing).
## General flow (step-by-step)

1. Trigger: `When clicking 'Test workflow'` — start the flow.
2. `Configuration` sets runtime variables (owner, repo, branch, processingMode, batchSize, fetchFileContent, maxFilesToProcess, testBranch).
3. `Get Branch Info` and `Get Repository Tree` fetch repository metadata and full file tree.
4. `Process File Structure` filters potential source files (by extension and excluded folders), sets `sourceFiles` and `sourceFilesCount`, and applies `maxFilesToProcess`.
5. `Route by Processing Mode`:
   - If `individual`: split into single-file items and analyze each file separately (`Fetch File Content` -> `Prepare Individual File Prompt` -> `AI - Individual File Analysis`).
   - If `batch`: `Create Batches` groups files into batches of `batchSize` and runs `AI - Batch Analysis`.
6. `Merge All Results` collects AI outputs (from individual or batch paths).
7. `Format Final Output` parses and normalizes AI responses into a well-structured JSON with fields such as `repository`, `processingMode`, `summary`, and `testFiles` (each file includes `testFileContent`, `testFile`, `runCommand`, etc.).
   - If parsing issues are encountered, `errors` are returned in the summary (the workflow includes robust parsing code to handle template literals and common malformed responses).
8. `Export to JSON File` writes consolidated results locally.
9. (Optional) The flow then enriches each `testFile` with repo context, creates test files locally, and pushes them to the configured `testBranch` on GitHub.
10. When the workflow complete, the webhook of n8n will be called and send some "sample" files into a predefined email.

## Future work

1. The user can received email should be configurable.
2. Send the valuable information of the test result artifact, because currently the attached file in email does not give enough insigt for user.
