# VSC Essentials Core - Pack for VSCode

[![Badge for version for Visual Studio Code extension](https://flat.badgen.net/vs-marketplace/v/Gydunhn.vsc-essentials-core?icon=visualstudio&color=blue)](https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials-core) [![Installs](https://flat.badgen.net/vs-marketplace/i/Gydunhn.vsc-essentials-core?color=blue)](https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials-core) [![Downloads](https://flat.badgen.net/vs-marketplace/d/Gydunhn.vsc-essentials-core?color=blue)](https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials-core) [![Rating](https://flat.badgen.net/vs-marketplace/rating/Gydunhn.vsc-essentials-core?color=blue)](https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials-core)

This extension pack for Visual Studio Code adds extensions that are convenient and useful for any development (regardless of language). I reserve the right to update the content of the extension pack at my own discretion.

This **BASIC** version of the extension pack is for a series of very specific projects in which I am currently involved; projects with multiple repositories that share the same stack of technologies transversally.

## Reasons

The "Original" [VSC Essentials] extension pack was made to automate and standardize the setup phase of the development environment for Visual Studio Code, to have the same set of extensions, use the same id settings and file format everyone works on together.

See the [CHANGELOG](https://github.com/Gydunhn/VSC-Essentials/blob/HEAD/CHANGELOG.md) for the latest changes

## **settings.json**

It is imperative that the settings be added to settings.json, inside the ".vscode" folder, and that this file be inside Git version control for this extension pack to work correctly.

``` json
{
    "extensions.ignoreRecommendations": true,
    "editor.tabCompletion": "on",
    "editor.showDeprecated": true,
    "editor.rulers": [
        80
    ],
    "editor.guides.bracketPairs": "active",
    "editor.bracketPairColorization.independentColorPoolPerBracketType": true,
    "workbench.tree.expandMode": "singleClick",
    "workbench.tree.renderIndentGuides": "always",
    "workbench.tree.indent": 6,
    "editor.formatOnType": false,
    "editor.formatOnSave": true,
    "editor.formatOnPaste": true,
    "[markdown]": {
        "editor.defaultFormatter": "yzhang.markdown-all-in-one"
    },
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    "[xml]": {
        "editor.defaultFormatter": "DotJoshJohnson.xml"
    },
    "[javascript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "[typescript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "[css]": {
        "editor.defaultFormatter": "vscode.css-language-features"
    },
    "[less]": {
        "editor.defaultFormatter": "vscode.css-language-features"
    },
    "[scss]": {
        "editor.defaultFormatter": "vscode.css-language-features"
    },
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    },
    "javascript.format.enable": true,
    "javascript.format.semicolons": "insert",
    "javascript.preferences.quoteStyle": "single",
    "typescript.format.enable": true,
    "typescript.format.semicolons": "insert",
    "typescript.preferences.quoteStyle": "single",
    "css.hover.documentation": true,
    "css.lint.important": "warning",
    "css.lint.importStatement": "warning",
    "less.hover.documentation": true,
    "less.lint.important": "warning",
    "less.lint.importStatement": "warning",
    "scss.hover.documentation": true,
    "scss.lint.important": "warning",
    "scss.lint.importStatement": "warning",
    "html.hover.documentation": true,
    "markdownlint.config": {
        "default": true,
        "MD001": false,
        "MD010": false,
        "MD024": false,
        "MD025": false
    }
}
```

## Note

This extension pack was made from their original [VSC Essentials], which you can find [here]

## Included

This **Basic** Core extension pack includes the following extensions:

| Extension           | Stats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Markdown All in One | [![Badge for version for Visual Studio Code extension](https://flat.badgen.net/vs-marketplace/v/yzhang.markdown-all-in-one?icon=visualstudio&color=blue)](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) [![Installs](https://flat.badgen.net/vs-marketplace/i/yzhang.markdown-all-in-one?color=blue)](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) [![Rating](https://flat.badgen.net/vs-marketplace/rating/yzhang.markdown-all-in-one?color=blue)](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)                         |
| markdownlint        | [![Badge for version for Visual Studio Code extension](https://flat.badgen.net/vs-marketplace/v/DavidAnson.vscode-markdownlint?icon=visualstudio&color=blue)](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) [![Installs](https://flat.badgen.net/vs-marketplace/i/DavidAnson.vscode-markdownlint?color=blue)](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) [![Rating](https://flat.badgen.net/vs-marketplace/rating/DavidAnson.vscode-markdownlint?color=blue)](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) |
| XML Tools           | [![Badge for version for Visual Studio Code extension](https://flat.badgen.net/vs-marketplace/v/DotJoshJohnson.xml?icon=visualstudio&color=blue)](https://marketplace.visualstudio.com/items?itemName=DotJoshJohnson.xml) [![Installs](https://flat.badgen.net/vs-marketplace/i/DotJoshJohnson.xml?color=blue)](https://marketplace.visualstudio.com/items?itemName=DotJoshJohnson.xml) [![Rating](https://flat.badgen.net/vs-marketplace/rating/DotJoshJohnson.xml?color=blue)](https://marketplace.visualstudio.com/items?itemName=DotJoshJohnson.xml)                                                                         |

[vsc essentials]: https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials
[here]: https://marketplace.visualstudio.com/items?itemName=Gydunhn.vsc-essentials