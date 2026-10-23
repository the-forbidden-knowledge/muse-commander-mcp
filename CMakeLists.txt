cmake_minimum_required(VERSION 3.24)

project(NativeBeam LANGUAGES CXX)

if(NOT WIN32 OR NOT MSVC)

  message(FATAL_ERROR "Use Windows x64 e Microsoft C++ Build Tools")

endif()

set(WEBVIEW2_DIR "${CMAKE_SOURCE_DIR}/.tools/webview2" CACHE PATH "WebView2 SDK")

add_executable(NativeBeam WIN32 native/main.cpp native/app.rc)

target_compile_features(NativeBeam PRIVATE cxx_std_20)

target_compile_definitions(NativeBeam PRIVATE UNICODE _UNICODE WIN32_LEAN_AND_MEAN NOMINMAX)

target_compile_options(NativeBeam PRIVATE /W4 /utf-8 /EHsc)

target_include_directories(NativeBeam PRIVATE "${WEBVIEW2_DIR}/build/native/include")

target_link_libraries(NativeBeam PRIVATE "${WEBVIEW2_DIR}/build/native/x64/WebView2LoaderStatic.lib" ole32 oleaut32 user32 shlwapi shell32 version uuid)

set_property(TARGET NativeBeam PROPERTY MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")

set_target_properties(NativeBeam PROPERTIES

  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/Release"

  RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_BINARY_DIR}/Release"

)
