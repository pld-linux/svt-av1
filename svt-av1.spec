# TODO: system cpuinfo (when released? note: different project than packaged in cpuinfo.spec)
Summary:	Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder)
Summary(pl.UTF-8):	Scalable Video Technology dla AV1 (koder i dekoder SVT-AV1)
Name:		svt-av1
Version:	3.0.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://gitlab.com/AOMediaCodec/SVT-AV1/-/releases
Source0:	https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v%{version}/SVT-AV1-v%{version}.tar.bz2
# Source0-md5:	f5ba568f3ea6b57c6d315957265d69d7
URL:		https://gitlab.com/AOMediaCodec/SVT-AV1
BuildRequires:	cmake >= 3.16
BuildRequires:	libstdc++-devel >= 6:5.4
BuildRequires:	rpmbuild(macros) >= 1.605
%ifarch %{x8664}
# or yasm >= 1.2.0
BuildRequires:	nasm >= 2.14
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
%attr(755,root,root) %{_bindir}/SvtAv1EncApp
%attr(755,root,root) %{_libdir}/libSvtAv1Enc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSvtAv1Enc.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSvtAv1Enc.so
# dir also used by svt-av1-dec built from older package
%dir %{_includedir}/svt-av1
%{_includedir}/svt-av1/EbDebugMacros.h
%{_includedir}/svt-av1/EbSvtAv1.h
%{_includedir}/svt-av1/EbSvtAv1Enc.h
%{_includedir}/svt-av1/EbSvtAv1ErrorCodes.h
%{_includedir}/svt-av1/EbSvtAv1Formats.h
%{_includedir}/svt-av1/EbSvtAv1Metadata.h
%{_pkgconfigdir}/SvtAv1Enc.pc
