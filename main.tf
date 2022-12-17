terraform {
  backend "remote" {
    organization = "pks-org"
    workspaces {
      name = "forum-workspace"
    }
  }
}

resource "null_resource" "example" {
  triggers = {
    value = "A example resource that does nothing!"
  }
}