return {
	cmd = { 'gopls' },
	filetypes = { 'go' },
	root_markers = {
		"requirements.txt",
		".git",
		"go.mod"
	},
	settings = {
		gopls = {
			analyses = {
				uunusedparams = true,
				shadow = true,
			},

		},
	},
}



