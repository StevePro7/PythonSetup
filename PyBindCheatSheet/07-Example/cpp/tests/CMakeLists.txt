# ---- GoogleTest ----
include(FetchContent)
FetchContent_Declare(
        googletest
        GIT_REPOSITORY https://github.com/google/googletest.git
        GIT_TAG v1.14.0
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
include(GoogleTest)

# Ensure Python dev target is available for linking (Python C API symbols)
find_package(Python3 REQUIRED COMPONENTS Development)

# ---- Helper function ----
function(add_my_test target)
    add_executable(${target} ${ARGN})

    target_link_libraries(${target}
            PRIVATE
            my_api
            GTest::gtest_main
            Python3::Python
            )

    gtest_discover_tests(${target})
endfunction()

# ---- Tests ----
add_my_test(tests_matrix test_matrix.cpp)
add_my_test(tests_vector test_vector.cpp)
add_my_test(tests_mesh test_mesh.cpp)
add_my_test(tests_mesh_algorithms test_mesh_algorithms.cpp)

# Special case (needs gmock)
add_executable(tests_mesh_processor test_mesh_processor.cpp)
target_link_libraries(tests_mesh_processor
        PRIVATE
        my_api
        GTest::gtest_main
        GTest::gmock_main
        Python3::Python
        )
gtest_discover_tests(tests_mesh_processor)
