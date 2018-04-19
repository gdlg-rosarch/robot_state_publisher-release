# Script generated with Bloom
pkgdesc="ROS - This package allows you to publish the state of a robot to <a href="http://ros.org/wiki/tf">tf</a>. Once the state gets published, it is available to all components in the system that also use <tt>tf</tt>. The package takes the joint angles of the robot as input and publishes the 3D poses of the robot links, using a kinematic tree model of the robot. The package can both be used as a library and as a ROS node. This package has been well tested and the code is stable. No major changes are planned in the near future."
url='http://wiki.ros.org/robot_state_publisher'

pkgname='ros-melodic-robot-state-publisher'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-melodic-catkin'
'ros-melodic-kdl-parser'
'ros-melodic-orocos-kdl>=1.3.0'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-rostest'
'ros-melodic-rostime'
'ros-melodic-sensor-msgs'
'ros-melodic-tf'
'ros-melodic-tf2-kdl'
'ros-melodic-tf2-ros'
'urdfdom-headers'
)

depends=('eigen3'
'ros-melodic-catkin'
'ros-melodic-kdl-parser'
'ros-melodic-orocos-kdl>=1.3.0'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-rostime'
'ros-melodic-sensor-msgs'
'ros-melodic-tf'
'ros-melodic-tf2-kdl'
'ros-melodic-tf2-ros'
)

conflicts=()
replaces=()

_dir=robot_state_publisher
source=()
md5sums=()

prepare() {
    cp -R $startdir/robot_state_publisher $srcdir/robot_state_publisher
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

