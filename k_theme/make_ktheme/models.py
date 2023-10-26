# from django.db import models
# from django.contrib.auth.models import User
# import os
# import shutil
# from django.conf import settings

# # from main.models import Ktheme


# def ktheme_save_path(instance, filename):
#     return os.path.join("kthemes", str(instance.user.id), filename)


# class Ktheme(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     # user_id = models.CharField(max_length=50)
#     theme_name = models.CharField(max_length=50)
#     theme_id = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.theme_name} by {self.user.username}"

#     # image_dir = models.CharField(max_length=255, black=True)
#     def theme_dir(self):
#         return os.path.join(settings.MEDIA_ROOT, self.user.username, self.theme_name)

#     def create_dir(self):
#         theme_dir_path = self.theme_dir()
#         os.makedires(theme_dir_path, exist_ok=True)

#         image_dir_path = os.path.join(theme_dir_path, "Images")
#         os.makedires(image_dir_path, exist_ok=True)

#         src_dir_path = os.path.join(settings.STATIC_ROOT, "Images")

#         for filename in os.listdir(src_dir_path):
#             src_image_path = os.path.join(src_dir_path, filename)
#             dest_image_path = os.path.join(image_dir_path, filename)
#             shutil.copy2(src_image_path, dest_image_path)

#     # def dir_path(self):
#     #     return f"media/{self.user_id}/{self.theme_name}"


# class CssColor(models.Model):
#     ktheme = models.OneToOneField(Ktheme, on_delete=models.CASCADE)
#     bg_color = models.CharField(max_length=7, default="#FFFFFF")
#     main_text_color = models.CharField(max_length=7, default="#000000")
#     point_text_color = models.CharField(max_length=7, default="#FFC0CB")
#     input_bg_color = models.CharField(max_length=7, default="#D3D3D3")
#     send_text_color = models.CharField(max_length=7, default="#A9A9A9")
#     receive_text_color = models.CharField(max_length=7, default="#808080")


# class CssBubble(models.Model):
#     ktheme = models.OneToOneField(Ktheme, on_delete=models.CASCADE)
#     s_1_x = models.PositiveIntegerField(default=17)
#     s_1_y = models.PositiveIntegerField(default=17)
#     s_1_t = models.PositiveIntegerField(default=10)
#     s_1_l = models.PositiveIntegerField(default=11)
#     s_1_b = models.PositiveIntegerField(default=9)
#     s_1_r = models.PositiveIntegerField(default=17)

#     s_2_x = models.PositiveIntegerField(default=17)
#     s_2_y = models.PositiveIntegerField(default=17)
#     s_2_t = models.PositiveIntegerField(default=10)
#     s_2_l = models.PositiveIntegerField(default=11)
#     s_2_b = models.PositiveIntegerField(default=9)
#     s_2_r = models.PositiveIntegerField(default=17)

#     r_1_x = models.PositiveIntegerField(default=20)
#     r_1_y = models.PositiveIntegerField(default=17)
#     r_1_t = models.PositiveIntegerField(default=10)
#     r_1_l = models.PositiveIntegerField(default=17)
#     r_1_b = models.PositiveIntegerField(default=9)
#     r_1_r = models.PositiveIntegerField(default=11)

#     r_2_x = models.PositiveIntegerField(default=20)
#     r_2_y = models.PositiveIntegerField(default=17)
#     r_2_t = models.PositiveIntegerField(default=10)
#     r_2_l = models.PositiveIntegerField(default=17)
#     r_2_b = models.PositiveIntegerField(default=9)
#     r_2_r = models.PositiveIntegerField(default=11)


# # class Ktheme(models.Model):
# #     # Images directory
# #     dir_path = models.CharField(max_length=500)

# #     # bubble px
# #     s_1_x = models.PositiveIntegerField(blank=True, null=True)
# #     s_1_y = models.PositiveIntegerField(blank=True, null=True)
# #     s_1_t = models.PositiveIntegerField(blank=True, null=True)
# #     s_1_l = models.PositiveIntegerField(blank=True, null=True)
# #     s_1_b = models.PositiveIntegerField(blank=True, null=True)
# #     s_1_r = models.PositiveIntegerField(blank=True, null=True)

# #     s_2_x = models.PositiveIntegerField(blank=True, null=True)
# #     s_2_y = models.PositiveIntegerField(blank=True, null=True)
# #     s_2_t = models.PositiveIntegerField(blank=True, null=True)
# #     s_2_l = models.PositiveIntegerField(blank=True, null=True)
# #     s_2_b = models.PositiveIntegerField(blank=True, null=True)
# #     s_2_r = models.PositiveIntegerField(blank=True, null=True)

# #     r_1_x = models.PositiveIntegerField(blank=True, null=True)
# #     r_1_y = models.PositiveIntegerField(blank=True, null=True)
# #     r_1_t = models.PositiveIntegerField(blank=True, null=True)
# #     r_1_l = models.PositiveIntegerField(blank=True, null=True)
# #     r_1_b = models.PositiveIntegerField(blank=True, null=True)
# #     r_1_r = models.PositiveIntegerField(blank=True, null=True)

# #     r_2_x = models.PositiveIntegerField(blank=True, null=True)
# #     r_2_y = models.PositiveIntegerField(blank=True, null=True)
# #     r_2_t = models.PositiveIntegerField(blank=True, null=True)
# #     r_2_l = models.PositiveIntegerField(blank=True, null=True)
# #     r_2_b = models.PositiveIntegerField(blank=True, null=True)
# #     r_2_r = models.PositiveIntegerField(blank=True, null=True)

# #     # css
# #     # theme_id = models.CharField(max_length=100)
# #     # theme_name = models.CharField(max_length=100)
# #     bg_color = models.CharField(max_length=7, default="#FFFFFF", null=True, blank=True)
# #     main_text_color = models.CharField(
# #         max_length=7, default="#000000", null=True, blank=True
# #     )
# #     point_text_color = models.CharField(
# #         max_length=7, default="#FFC0CB", null=True, blank=True
# #     )
# #     input_bg_color = models.CharField(
# #         max_length=7, default="#D3D3D3", null=True, blank=True
# #     )
# #     send_text_color = models.CharField(
# #         max_length=7, default="#A9A9A9", null=True, blank=True
# #     )
# #     receive_text_color = models.CharField(
# #         max_length=7, default="#808080", null=True, blank=True
# #     )
