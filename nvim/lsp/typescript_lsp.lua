
return {
	cmd = { 'typescript-language-server', "--stdio"},
	filetypes = {
        "javascript",
        "javascriptreact",
        "javascript.jsx",
        "typescript",
        "typescriptreact",
        "typescript.tsx"
    },
	root_markers = {
        "package.json",
        "tsconfig.json",
        ".git"
	},
	settings = {
        typescript = {
            preferences = {
                includePackageJsonAutoImports = "auto",
                includeInlayParameterNameHints = "literals",
            },
        },
        javascript = {
            preferences = {
                includePackageJsonAutoImports = "auto",
                includeInlayParameterNameHints = "literals",
            },
        },
	},
}
