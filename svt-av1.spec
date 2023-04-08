Summary:	Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder)
Summary(pl.UTF-8):	Scalable Video Technology dla AV1 (koder i dekoder SVT-AV1)
Name:		svt-av1
Version:	1.4.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://gitlab.com/AOMediaCodec/SVT-AV1/-/releases
Source0:	https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v%{version}/SVT-AV1-v%{version}.tar.bz2
# Source0-md5:	10fbfc2da4f02bdcecdb3d5fba341e78
URL:		https://gitlab.com/AOMediaCodec/SVT-AV1
BuildRequires:	cmake >= 3.16
BuildRequires:	libstdc++-devel >= 6:5.4
BuildRequires:	rpmbuild(macros) >= 1.605
%ifarch %{x8664}
# or nasm >= 2.14
BuildRequires:	yasm >= 1.2.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder) is
an AV1-compliant encoder/decoder library core. The SVT-AV1 encoder
development is a work-in-progress targeting performance levels
applicable to both VOD and Live encoding/transcoding video
applications. The SVT-AV1 decoder implementation is targeting future
codec research activities.

%description -l pl.UTF-8
Scalable Video Technology dla AV1 (koder i dekoder SVT-AV1) to główna
biblioteka kodera/dekodera zgodnego z AV1. Rozwój kodera SVT-AV1 trwa,
a jego celem jest osiągnięcie wydajności nadającej się do kodowania i
przekodowywania obrazu zarówno VOD, jak i w czasie rzeczywistym.
Implementacja dekodera ma na celu dalsze badania nad kodekiem.

%package devel
Summary:	Header files for SVT-AV1 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SVT-AV1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SVT-AV1 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SVT-AV1.

%prep
%setup -q -n SVT-AV1-v%{version}

%build
%cmake -B build \
%ifnarch %{x8664}
	-DCOMPILE_C_ONLY=ON
%endif

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.md PATENTS.md README.md 
%attr(755,root,root) %{_bindir}/SvtAv1DecApp
%attr(755,root,root) %{_bindir}/SvtAv1EncApp
%attr(755,root,root) %{_libdir}/libSvtAv1Dec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSvtAv1Dec.so.0
%attr(755,root,root) %{_libdir}/libSvtAv1Enc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSvtAv1Enc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSvtAv1Dec.so
%attr(755,root,root) %{_libdir}/libSvtAv1Enc.so
%{_includedir}/svt-av1
%{_pkgconfigdir}/SvtAv1Dec.pc
%{_pkgconfigdir}/SvtAv1Enc.pc
