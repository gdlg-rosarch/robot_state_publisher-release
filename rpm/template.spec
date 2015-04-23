Name:           ros-jade-robot-state-publisher
Version:        1.10.4
Release:        0%{?dist}
Summary:        ROS robot_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/robot_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-catkin
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-orocos-kdl >= 1.3.0
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-rostime
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-kdl-parser
BuildRequires:  ros-jade-orocos-kdl >= 1.3.0
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Apr 23 2015 Ioan Sucan <isucan@google.com> - 1.10.4-0
- Autogenerated by Bloom

