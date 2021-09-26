find_package(OpenMP)

if(NOT OpenMP_C_FOUND)
    message(FATAL_ERROR "Cannot find OpenMP for C language")
endif()

set(_include_dir ${CMAKE_CURRENT_SOURCE_DIR}/include)


file(GLOB_RECURSE _headers RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} ${_include_dir}/*.h*)

add_executable(${PROJECT_NAME} ${_headers} ${CMAKE_CURRENT_SOURCE_DIR}/src/matmul.c)
set_property(TARGET ${PROJECT_NAME} PROPERTY C_STANDARD 11)

target_include_directories(${PROJECT_NAME} PRIVATE ${_include_dir})
target_link_libraries(${PROJECT_NAME} PRIVATE OpenMP::OpenMP_C)
unset(_include_dir)
