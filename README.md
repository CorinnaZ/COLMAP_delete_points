# COLMAP_delete_points
Provides a function to delete image ids from points3D.txt file for COLMAP

When you use the image_deleter provided by COLMAP, all points that are not seen by every remaining image are deleted. This function takes a points3D.txt file as an input and deletes only the points that are seen from none of the remaining images.
