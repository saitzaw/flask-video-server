# check the opeartion system 
# Test only in Ubuntu 
# This shell script is a helper for python

# check the OS 
function check_os() {
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi
} 

# Installation 
# need the super use access 
# Support for Ubuntu, Mint, CentOS, Fedora 
# Use the precompile ffmpeg 
function detect_os {
    case ${OS} in 
    Ubuntu)
    package_install_deb
    ;; 
    LinuxMint)
    package_install_deb
    ;; 
    CentOS) 
    package_install_rpm_centos
    ;; 
    Fedora) 
    package_install_rpm_fedora
    ;;
    *) 
    echo -n "Cannot support ${OS} and ${VER} yet"
    ;;
    esac 
}

# for DEB package 
function package_install_deb() {
    sudo apt -oDebug::pkgAcquire::Worker=1 update 
    sudo apt install ffmpeg
}

# for RPM package 
# for centso 
function package_install_rpm_centos {
    sudo yum install epel-release -y 
    sudo yum update 
    sudo rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
    sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
    sudo yum install ffmpeg ffmpeg-devel -y
}

# for fedora 
function package_install_rpm_fedora {
    sudo dnf install \
    https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
    https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

    sudo dnf update 
    sudo dnf install ffmpeg
}

# invoke the check function 
check_os 
detect_os 


