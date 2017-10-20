Name:       libgee

Summary:    GObject collection library
Version:    0.20.0
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://live.gnome.org/Libgee
Source0:    http://download.gnome.org/sources/%{name}/0.6/%{name}-%{version}.tar.xz
Patch0:     0001-fix-broken-sed.patch
# Our Gnome building isn't new enough for this
# AX_REQUIRE_DEFINED([GOBJECT_INTROSPECTION_CHECK]) causes a build error
Patch1:     0002-revert-move-away-from-gnome-common.patch

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  vala-devel >= 0.24
BuildRequires:  vala-tools >= 0.24
BuildRequires:  gobject-introspection-devel >= 1.36
BuildRequires:  gnome-common

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   vala

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-fix-broken-sed.patch
%patch0 -p1
# 0002-revert-move-away-from-gnome-common.patch
%patch1 -p1

echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make

%build
touch ChangeLog
USE_GNOME2_MACROS=1 NOCONFIGURE=1 gnome-autogen.sh
%autogen --disable-static
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gee-0.8.pc
%{_datadir}/vala/vapi/gee-0.8.vapi
%{_datadir}/gir-1.0/Gee-0.8.gir
