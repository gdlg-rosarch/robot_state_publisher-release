Name:           ros-kinetic-robot-state-publisher
Version:        1.13.1
Release:        0%{?dist}
Summary:        ROS robot_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-catkin
Requires:       ros-kinetic-kdl-parser
Requires:       ros-kinetic-orocos-kdl >= 1.3.0
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rostime
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2-kdl
Requires:       ros-kinetic-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-kdl-parser
BuildRequires:  ros-kinetic-orocos-kdl >= 1.3.0
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rostime
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2-kdl
BuildRequires:  ros-kinetic-tf2-ros

%description
This package allows you to publish the state of a robot to tf. Once the state
gets published, it is available to all components in the system that also use
tf. The package takes the joint angles of the robot as input and publishes the
3D poses of the robot links, using a kinematic tree model of the robot. The
package can both be used as a library and as a ROS node. This package has been
well tested and the code is stable. No major changes are planned in the near
future

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri May 20 2016 Ioan Sucan <isucan@google.com> - 1.13.1-0
- Autogenerated by Bloom

* Tue Apr 12 2016 Ioan Sucan <isucan@google.com> - 1.13.0-0
- Autogenerated by Bloom

