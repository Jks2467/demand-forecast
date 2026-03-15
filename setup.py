import setuptools

__version__ = "0.0.0"

REPO_NAME = ""
AUTHOR_USER_NAME = "Jks2467"
SRC_REPO = ""
AUTHOR_EMAIL = "jksharma2467@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Demand Forecast XGBoost model",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

