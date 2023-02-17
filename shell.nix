{ pkgs ? import <nixpkgs> {}}:
with pkgs;
mkShell {
  buildInputs = [
    python310
  ] ++ (with pkgs.python310Packages; [
    lxml
    requests
    beautifulsoup4
  ]);
}
