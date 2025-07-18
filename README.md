# SVD Image Compression

This project demonstrates **image compression using Singular Value Decomposition (SVD)** with Python's NumPy and Matplotlib libraries. It visualizes how different ranks (r) affect image reconstruction quality and storage efficiency.

## 📷 Overview

- Converts an RGB image to grayscale.
- Performs SVD decomposition.
- Reconstructs compressed images with different numbers of singular values.
- Displays:
  - Original image
  - Compressed images with various `r` values
  - Singular value distribution (log scale)
  - Cumulative sum of singular values to analyze compression coverage

## 📝 Dependencies

- Python 3.x
- NumPy
- Matplotlib

Install dependencies using:

<pre> ```bash pip install numpy matplotlib git clone https://github.com/yourusername/svd-image-compression.git cd svd-image-compression ``` </pre>

markdown
Copy
Edit

2. **Add your image file:**

Replace `'images.jpg'` in the code with your desired image file path.

3. **Run the script:**

python svd_image_compression.py

markdown
Copy
Edit

4. **Output:**

- A grid plot showing:
  - The original image
  - Compressed images with ranks `[1, 5, 20, 50, 100, 200, 400]`
- Singular values plot (semilog)
- Cumulative sum plot of singular values

## 🤔 How it works

- **Singular Value Decomposition (SVD)** breaks the image matrix into three matrices: `U`, `S`, and `VT`.
- By keeping only the top `r` singular values and corresponding vectors, you can approximate the original image with reduced data while preserving essential features.

## 💡 Applications

- Image compression
- Noise reduction
- Dimensionality reduction in data science

## 📝 License

This project is open-source and available under the MIT License.

---

**Feel free to fork, modify, and experiment with different images and r values!**

