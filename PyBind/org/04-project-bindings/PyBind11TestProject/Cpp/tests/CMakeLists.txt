include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

add_executable(test_hello test_hello.cpp)
target_link_libraries(test_hello PRIVATE myproject_cpp gtest_main)

add_test(NAME test_hello COMMAND test_hello)
