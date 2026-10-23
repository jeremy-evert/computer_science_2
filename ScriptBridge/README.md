# ScriptBridge — Browser Edition

This folder contains the static website version of ScriptBridge. It runs in the visitor's browser and does not need a server-side app or terminal.

## Publish with GitHub Pages

1. Create a GitHub repository for the website and upload the contents of this folder. Keep `index.html` at the repository root.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select the `main` branch and `/ (root)`, then save.
4. Wait for the Pages deployment to finish. GitHub will show the website address in the Pages settings.

## Browser edition limits

- Basic checks are hints, not full language validation. This edition does not have every feature of the Windows version. GitHub Pages cannot run the local Ruff helper, so Python checks here are basic, not full linting. This edition does not run submitted scripts.
- File open/save buttons need a supported browser, such as current Chrome or Edge. GitHub Pages serves over HTTPS, which allows the browser's file picker APIs where supported. The browser asks the visitor to choose and authorize files; scripts are edited on the visitor's device.
- Browser storage, including saved-version history, stays in that browser on that device.
- The Windows Ruff helper, its executable, and its launcher are intentionally not part of this website folder. GitHub Pages is static hosting and cannot run those Windows components.

The downloadable Windows package remains separate in `ScriptBridge-rebuilt`.

