Name:           ros-indigo-motoman-sia5d-support
Version:        0.3.5
Release:        0%{?dist}
Summary:        ROS motoman_sia5d_support package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/motoman_sia5d_support
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-motoman-driver
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-rviz
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
ROS Industrial support for the Motoman sia5d (and variants). This package
contains configuration data, 3D models and launch files for Motoman sia5d
manipulators. Specifications sia5d - Default Joint limits and maximum joint
velocities are based on the information found in the online
http://www.motoman.com/datasheets/sia5d.pdf All urdfs are based on the default
motion and joint velocity limits, unless noted otherwise. Before using any of
the configuration files and / or meshes included in this package, be sure to
check they are correct for the particular robot model and configuration you
intend to use them with.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jul 03 2016  <shaun.edwards@gmail.com> - 0.3.5-0
- Autogenerated by Bloom

