Name:       libgee

Summary:    GObject collection library
Version:    0.20.6
Release:    1
License:    LGPLv2+
URL:        http://live.gnome.org/Libgee
Source0:    %{name}-%{version}.tar.xz
Patch0:     0001-Our-old-sed-does-not-support-E-work-around-it.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  vala-devel >= 0.24
BuildRequires:  vala-tools >= 0.24
BuildRequires:  gobject-introspection-devel >= 1.36

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.


%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   vala

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./autogen.sh --disable-doc --disable-static --disable-internal-asserts --prefix=%{_prefix} --libdir=%{_libdir}
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gee-0.8.pc
%{_datadir}/vala/vapi/gee-0.8.vapi
%{_datadir}/gir-1.0/Gee-0.8.gir
