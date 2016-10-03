project(hello)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if (MSVC)
    set (CMAKE_CXX_FLAGS "/bigobj")
endif ()

add_executable(hello main.cpp)
target_link_libraries(hello ${CONAN_LIBS})
