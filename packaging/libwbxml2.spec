Name:           libwbxml2
Version:        0.11.2
Release:        1
License:        LGPL-2.1+
Summary:        WBXML parser and compiler library
Url:            http://libwbxml.opensync.org/
Group:          System/Libraries
Source:         libwbxml-%{version}.tar.bz2
Source1001: 	libwbxml2.manifest
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)

%description
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.

%package -n wbxml2-tools
License:        GPL-2.0+
Summary:        Tools for libwbxml2
Group:          System/Utilities
Requires:       pkgconfig(libxml-2.0)
Requires:       %{name} = %{version}

%description -n wbxml2-tools
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.

%package devel
License:        LGPL-2.1+
Summary:        WBXML parser and compiler library
Group:          System/Development
Requires:       glibc-devel
Requires:       libwbxml2 = %{version}
Requires:       pkgconfig(expat)
Requires:       pkgconfig(libxml-2.0)

%description devel
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.

%prep
%setup -q -n libwbxml-%{version}
cp %{SOURCE1001} .

%build
mkdir build
pushd build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
%cmake \
        -DCMAKE_BUILD_TYPE=None \
        -DENABLE_INSTALL_DOC:BOOL=OFF \
         %{_builddir}/libwbxml-%{version}
make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd build
%make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%{_libdir}/libwbxml2.so.1*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/pkgconfig/libwbxml2.pc
%{_libdir}/libwbxml2.so
%{_includedir}/libwbxml-1.0/wbxml
%{_datadir}/cmake/Modules/FindLibWbxml2.cmake
%{_includedir}/wbxml_config.h

%files -n wbxml2-tools
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/wbxml2xml
%{_bindir}/xml2wbxml

%changelog
