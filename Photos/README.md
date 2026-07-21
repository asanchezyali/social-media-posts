# Photos — cover source pool

Source photos for the **Instagram** carousel covers (and any post that needs a
full-bleed photo). These are the originals; each post keeps its own baked copy at
`<Post>/assets/cover.jpg`, so renaming here never breaks a post.

## Naming

`<category>-NN.jpg` — lowercase, zero-padded, numbered by date within each
category. All normalized to `.jpg`.

| Category | What it is | Count |
|---|---|---|
| `work-NN` | Alejandro working at the laptop (cafés, coworking, patios) | 13 |
| `desk-NN` | Workspace setups — monitors, keyboard, notebook (no person) | 4 |
| `notes-NN` | Notebooks, tablets, papers, handwriting close-ups | 4 |
| `books-NN` | Bookshelf / a book on the desk | 2 |
| `cafe-NN` | Coffee / food on a café table | 3 |
| `nature-NN` | Landscapes (river, sunset) | 2 |
| `portrait-NN` | Portrait / selfie | 1 |

Most are **landscape** (4032×3024 / 3840×2160); `work-02…13` and `nature-01` are
**portrait**. The cover build crops any of them to 3:4 anyway.

## Using one as a cover

iPhone photos store orientation in EXIF that `\includegraphics` ignores, so bake
it in and crop to 3:4 (2160×2880) when placing a cover:

```bash
magick "Photos/work-05.jpg" -auto-orient -resize 2160x2880^ -gravity center \
  -extent 2160x2880  <Post>/assets/cover.jpg
```

Add a new photo as `<category>-<next-NN>.jpg` and it drops straight into the pool.
