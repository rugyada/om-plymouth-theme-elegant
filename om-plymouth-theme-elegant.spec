# noarch package but uses _lib macro in post scripts
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	"Openmandriva Elegant" Plymouth theme
Name:		om-plymouth-theme-elegant
Version:	2.0
Release:	1
License:	Creative Commons Attribution-ShareAlike
Group:		System/Kernel and hardware
URL:		https://github.com/rugyada/om-plymouth-theme-elegant
Source0:	%{name}-%version.tar.gz
Requires:	plymouth
Requires:	plymouth-plugin-script
Requires:	plymouth-scripts
Requires(post,postun):	plymouth-scripts


%description
This package contains the "OpenMandriva Elegant" Plymouth theme.

%files
%{_datadir}/plymouth/themes/openmandriva-elegant

%post
if [ -x %{_sbindir}/plymouth-set-default-theme ]; then
    export LIB=%{_lib}
    if [ $1 -eq 1 ]; then
        %{_sbindir}/plymouth-set-default-theme --rebuild-initrd openmandriva-elegant
    else
        THEME=$(%{_sbindir}/plymouth-set-default-theme)
        if [ "$THEME" == "text" -o "$THEME" == "openmandriva-elegant" ]; then
            %{_sbindir}/plymouth-set-default-theme --rebuild-initrd openmandriva-elegant
        fi
    fi
fi

%postun
export LIB=%{_lib}
if [ $1 -eq 0 -a -x %{_sbindir}/plymouth-set-default-theme ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "openmandriva-elegant" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset --rebuild-initrd
    fi
fi

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/

cp -r openmandriva-elegant %{buildroot}%{_datadir}/plymouth/themes/
