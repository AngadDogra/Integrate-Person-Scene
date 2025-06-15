# Integrate-Person-Scene

# Visit the Link : [Deployed Demo](https://angaddogra.pythonanywhere.com)

Photorealistic Placement Using Custom Image Blending Algorithm

# Overview
This project demonstrates an end-to-end image compositing workflow, placing a person into a new scene and ensuring realistic integration using advanced color, lighting, and shadow blending techniques. The result is presented via a simple Django web interface.

# Algorithm & Workflow
The core of this project is a multi-step photorealistic compositing pipeline:

# Foreground Extraction:

The person is photographed in controlled lighting.
Background is removed using modern segmentation tools (e.g., Photoshop, Remove.bg).

# Background Analysis:

The replacement scene’s shadows and lighting are analyzed, both visually and (optionally) programmatically using OpenCV.
Light Direction Estimation:

Key objects and their shadows are used to determine the main light source’s direction and elevation, ensuring realistic shadow casting for the new person.
Positioning & Scaling:

The person is carefully placed and sized in the background to match perspective and proportion.
Color, Tone, and Edge Blending:

The person’s image is color-corrected (brightness, color balance, and contrast) to align with the background scene.
Shadow is painted/matched according to the background’s geometry.
Edges are feathered, and “light wrapping” is applied for realism.
A global color grade is applied to the final composite for harmony.

# Final Presentation:

The before, background, and composite results are displayed together for easy visual comparison.

# Project Structure & Django Integration
The Django app serves as a front-end to showcase this image-processing workflow.
All output images (before.jpg, background.jpg, combined.jpg) are placed in the /media/ directory.

The main template displays the compositing results; navigation links are hidden for clarity.

No server-side processing is performed—images are created offline (using the described workflow) and simply displayed.

# How to Use
Replace or update images (before.jpg, background.jpg, combined.jpg) in your Django project’s media folder.
Run your Django server (or deploy on PythonAnywhere).
Browse the main page to view the compositing results and reference workflow.
References
Pérez, P., Gangnet, M., & Blake, A. (2003). Poisson image editing. ACM Transactions on Graphics.
Adobe, DxO, and CG Cookie online guides for professional compositing.
[See full references in project documentation.]
