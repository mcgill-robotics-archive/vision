# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "tld_msgs: 2 messages, 0 services")

set(MSG_I_FLAGS "-Itld_msgs:/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg;-Istd_msgs:/opt/ros/jade/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/jade/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/jade/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(tld_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" NAME_WE)
add_custom_target(_tld_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tld_msgs" "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" "sensor_msgs/Image:tld_msgs/BoundingBox:std_msgs/Header"
)

get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" NAME_WE)
add_custom_target(_tld_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tld_msgs" "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/sensor_msgs/cmake/../msg/Image.msg;/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg;/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tld_msgs
)
_generate_msg_cpp(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tld_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(tld_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tld_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(tld_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(tld_msgs_generate_messages tld_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_cpp _tld_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_cpp _tld_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tld_msgs_gencpp)
add_dependencies(tld_msgs_gencpp tld_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tld_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/sensor_msgs/cmake/../msg/Image.msg;/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg;/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tld_msgs
)
_generate_msg_eus(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tld_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(tld_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tld_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(tld_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(tld_msgs_generate_messages tld_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_eus _tld_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_eus _tld_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tld_msgs_geneus)
add_dependencies(tld_msgs_geneus tld_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tld_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/sensor_msgs/cmake/../msg/Image.msg;/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg;/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tld_msgs
)
_generate_msg_lisp(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tld_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(tld_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tld_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(tld_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(tld_msgs_generate_messages tld_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_lisp _tld_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_lisp _tld_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tld_msgs_genlisp)
add_dependencies(tld_msgs_genlisp tld_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tld_msgs_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/sensor_msgs/cmake/../msg/Image.msg;/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg;/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs
)
_generate_msg_py(tld_msgs
  "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/jade/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(tld_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(tld_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(tld_msgs_generate_messages tld_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/Target.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_py _tld_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alexsmith/coding/auv/catkin_ws/src/ros_opentld/tld_msgs/msg/BoundingBox.msg" NAME_WE)
add_dependencies(tld_msgs_generate_messages_py _tld_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tld_msgs_genpy)
add_dependencies(tld_msgs_genpy tld_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tld_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tld_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tld_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(tld_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(tld_msgs_generate_messages_cpp sensor_msgs_generate_messages_cpp)

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tld_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tld_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
add_dependencies(tld_msgs_generate_messages_eus std_msgs_generate_messages_eus)
add_dependencies(tld_msgs_generate_messages_eus sensor_msgs_generate_messages_eus)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tld_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tld_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(tld_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(tld_msgs_generate_messages_lisp sensor_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tld_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(tld_msgs_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(tld_msgs_generate_messages_py sensor_msgs_generate_messages_py)
