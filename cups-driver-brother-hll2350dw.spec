# TODO:
# - wrappers are INSANE doing copying, rming, guessing and other crazy things
%include        /usr/lib/rpm/macros.perl
Summary:	A set of CUPS printer drivers for Brother HL-L2352DW printer
Name:		cups-driver-brother-hll2350dw
Version:	4.0.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.brother.com/welcome/dlf103565/hll2350dwpdrv-%{version}-1.i386.rpm
# Source0-md5:	4d6261c7ca265f4ac88b7766faae3498
URL:		http://support.brother.com/g/b/downloadlist.aspx?c=pl&lang=pl&prod=hll2352dw_eu&os=127&flang=English
BuildRequires:	gzip
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-utils
Requires:	cups
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%(cups-config --datadir 2>/dev/null)
%define		_libdir		%(cups-config --serverbin 2>/dev/null)
%define		_cupsppddir	%{_datadir}/model
%define		_cupsfilterdir	%{_libdir}/filter

%description
CUPS driver for Brother HL-L2352DW.

%prep
%setup -qcT
rpm2cpio %{SOURCE0} | cpio -dimu

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_cupsppddir},%{_cupsfilterdir}}

cp -p opt/brother/Printers/HLL2350DW/cupswrapper/brother-HLL2350DW-cups-en.ppd $RPM_BUILD_ROOT%{_cupsppddir}
gzip $RPM_BUILD_ROOT%{_cupsppddir}/*.ppd

cp -p opt/brother/Printers/HLL2350DW/cupswrapper/lpdwrapper $RPM_BUILD_ROOT%{_cupsfilterdir}/brother_lpdwrapper_HLL2350DW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc opt/brother/Printers/HLL2350DW/LICENSE_ENG.txt
%{_cupsppddir}/brother-HLL2350DW-cups-en.ppd.gz
%attr(755,root,root) %{_cupsfilterdir}/brother_lpdwrapper_HLL2350DW
