ROHIT IMAGE STUDIO PRO — TERMUX

1. Extract ZIP in Termux:
   unzip Rohit_Image_Studio_Pro.zip
   cd rohit_image_studio_pro

2. Install Python if needed:
   pkg update -y
   pkg install python -y

3. Run:
   python server.py

4. Open:
   http://127.0.0.1:8080

Stop with Ctrl+C.

FEATURES
- Open a background image from the phone
- Add another picture as a movable layer
- Move and resize added pictures
- Add text, change text/font/size/color/outline
- Update selected text layer
- Paint over parts of the base image
- Delete added layers, reorder layers
- Undo/redo, reset, export PNG

LIMITATIONS
- This is a local manual editor, not a full Photoshop/AI editor.
- Replacing a picture means placing a new picture over the old one and sizing it manually.
- It cannot automatically detect and reconstruct the background behind an object or identify all text in a flattened photo. Paint-over uses a solid selected color, so complex backgrounds need a dedicated AI inpainting service.
- The original image is not sent to a server.

