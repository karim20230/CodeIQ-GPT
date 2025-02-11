import * as vscode from "vscode";
import axios from "axios"; // Install using `npm install axios`

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand("extension.analyzeCode", async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage("No open file.");
      return;
    }

    const code = editor.document.getText();
    const language = editor.document.languageId;
    
    const mode = await vscode.window.showQuickPick(["Explain", "Debug", "Autocomplete"], { placeHolder: "Select mode" });

    try {
      const response = await axios.post("http://localhost:8000/analyze_code", { mode, language, code });
      vscode.window.showInformationMessage("AI Response: " + response.data.response);
    } catch (error) {
      vscode.window.showErrorMessage("Error contacting AI assistant.");
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
