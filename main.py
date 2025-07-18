from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

# defining parameters
plt.rcParams['figure.figsize'] = [16, 10]
A = imread('images.jpg')
X = np.mean(A, -1) # Convert RGB to grayscale
U, S, VT = np.linalg.svd(X, full_matrices=False)
S = np.diag(S)
# Create 8 subplots to store original + 7 compressed variants
fig, ax = plt.subplots(2, 4, figsize=(16, 10))

# r_values = [1, 5, 20, 50, 100, 200, 400]
num_of_values = [1, 5, 20, 50, 100, 200, 400]
for i, r in enumerate(num_of_values):
    # Compute the approximate image using SVD
    img_approx = U[:, :r] @ S[0:r, :r] @ VT[:r, :]
    # Find row and column index for the subplot
    row = (i + 1) // 4
    col = (i + 1) % 4
    # Plot image on the subplot
    ax[row, col].imshow(img_approx, cmap='gray')
    ax[row, col].set_title(f"r = {r}")
    ax[row, col].axis("on")

# Plot the original image on the first subplot
ax[0, 0].imshow(A)
ax[0, 0].set_title("Original")
ax[0, 0].axis("off")
# Plot 7 compressed images with different r values on other subplots

plt.show()
plt.figure(2)
plt.semilogy(np.diag(S))
plt.title('Singular Values')
plt.show()
plt.figure(3)
plt.plot(np.cumsum(np.diag(S)) / np.sum(np.diag(S)))
plt.title('Singular Values: Cumulative Sum')
plt.show()
