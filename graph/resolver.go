package graph

import (
	"github.com/Jonathan-Zollinger/Gospel-TUI/graph/model"
)

// This file will not be regenerated automatically.
//
// It serves as dependency injection for your app, add any dependencies you require here.

type Resolver struct {
	verses   []*model.Verses
	chapters []*model.Chapters
	books    []*model.Books
	volumes  []*model.Volumes
}
