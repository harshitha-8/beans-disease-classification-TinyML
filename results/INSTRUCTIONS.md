# How to Add Result Images

## Instructions for Adding Your Result Images

1. **Save your result images** with the following names in the `results/` directory:
   - `result_1.png` - Training and validation accuracy plot
   - `result_2.png` - Training and validation loss plot
   - `result_3.png` - Confusion matrix
   - `result_4.png` - Sample prediction results

2. **Add the images to git:**
   ```bash
   git add results/result_1.png results/result_2.png results/result_3.png results/result_4.png
   git commit -m "Add result images"
   git push
   ```

3. **The images will automatically display** in the README.md file in a 2x2 table layout.

## Image Guidelines

- **Format**: PNG or JPG
- **Recommended size**: 800x600 pixels or similar aspect ratio
- **File naming**: Use `result_1.png`, `result_2.png`, etc. as specified above

## Adding More Images

To add additional result images beyond the initial 4:

1. Save them in the `results/` directory with descriptive names
2. Update the `results/README.md` to document them
3. Optionally, add them to the main README.md in the Results section

The results section is now ready for your images!
