add_library(MyProject SHARED core.cpp)

target_include_directories(MyProject PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set_target_properties(MyProject PROPERTIES POSITION_INDEPENDENT_CODE ON)

set_target_properties(MyProject PROPERTIES PREFIX "")
