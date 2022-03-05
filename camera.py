from arducam.camera_adapter import CameraAdapter, CAM_ROOT, CAM_SIDE, CAM_AERIAL

camera_adapter = CameraAdapter()

camera_adapter.change_camera(CAM_ROOT)
camera_adapter.capture('output/root_cam.jpg')

camera_adapter.change_camera(CAM_SIDE)
camera_adapter.capture('output/side_cam.jpg')

camera_adapter.change_camera(CAM_AERIAL)
camera_adapter.capture('output/aerial_cam.jpg')
