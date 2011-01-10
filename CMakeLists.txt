# ===============================
# CMake project file for TEARS
# ===============================
cmake_minimum_required(VERSION 2.6)

# ===============================
# Project Name
# ===============================
project(tears)

# ===============================
# Variables
# ===============================
file(
	GLOB_RECURSE
	python_libs
	lib/python/core/*
)

# ===============================
# Installation
# ===============================
install(PROGRAMS bin/tears.py DESTINATION bin)
install(FILES lib/python/argparse.py DESTINATION lib/python/)
install(FILES ${python_libs} DESTINATION lib/python/coccitools)
