from kivy_ios.toolchain import CythonRecipe


class MyRecipe(CythonRecipe):
    version = "master"
    url = "src"

    # Change the filename here. It could be anything as long as it
    # doesn't conflict with other libraries.
    library = "libmyrecipe.a"

    depends = ["python3", "hostpython3"]

    # Frameworks you used
    pbx_frameworks = ["Foundation", "UIKit"]

    def install(self):
        self.install_python_package(
            # Put the extension name here
            name=self.so_filename("myrecipe"), is_dir=False)


recipe = MyRecipe()
