Name:           libwbxml2
BuildRequires:  cmake gcc-c++ libexpat-devel pkg-config popt-devel zlib-devel
Url:            http://libwbxml.opensync.org/
License:        LGPL-2.1+
Group:          System/Libraries
Summary:        WBXML parser and compiler library
Version:        0.11.2
Release:        1
AutoReqProv:    on
Source:         libwbxml-%{version}.tar.bz2

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
Group:          Productivity/Other
Requires:       libwbxml2 = %{version} 

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
Group:          Development/Libraries/C and C++
Requires:       libwbxml2 = %{version} glibc-devel libexpat-devel 

%description devel 
wbxml2 is a library that includes a WBXML parser and a WBXML compiler.
Unlike wbxml, it does not depend on libxml2 but on expat, making it
faster and more portable. WBXML Library contains a library and its
associated tools to Parse, Encode and Handle WBXML documents. The WBXML
(Wireless Binary XML) format is a binary representation of XML, and it
has been defined by the Wap Forum.



%prep
%setup -q -n libwbxml-%{version}

%build
%__mkdir build
pushd build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
cmake \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DENABLE_INSTALL_DOC:BOOL=OFF \
%if %{_lib} == lib64
        -DLIB_SUFFIX=64 \
%endif
         %{_builddir}/libwbxml-%{version}
%__make %{?jobs:-j%jobs} VERBOSE=1
popd

%install
pushd build
%make_install
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-, root, root)
%doc COPYING
%{_libdir}/libwbxml2.so.1*

%files -n libwbxml2-devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/libwbxml2.pc
%{_libdir}/libwbxml2.so
%{_prefix}/include/libwbxml-1.0/wbxml
%{_datadir}/cmake/Modules/FindLibWbxml2.cmake

%files -n wbxml2-tools
%defattr(-,root,root)
%{_prefix}/bin/wbxml2xml
%{_prefix}/bin/xml2wbxml

%changelog
