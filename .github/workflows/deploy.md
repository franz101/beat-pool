name: Build Quartz Site
on:
 push:
   branches: ["main"]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Build
        uses: konstfish/quartz-build-action@v1
        with:
          source: content
          page_title: "BEAT-POOL PRODUCER MAP"
      - name: Free Up GitHub Actions Ubuntu Runner Disk Space 🔧
        uses: jlumbroso/free-disk-space@main
        with:
          # This might remove tools that are actually needed, if set to "true" but frees about 6 GB
          tool-cache: false
          # All of these default to true, but feel free to set to "false" if necessary for your workflow
          android: true
          dotnet: true
          haskell: true
          large-packages: true
          swap-storage: true
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}