%define name	scramble
%define version 4.5.0
%define release 9

Name: 	 	%{name}
Summary: 	File encryption utility used by xffm
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/xffm/%{name}-%{version}.tar.bz2
URL:		http://xffm.sf.net
License:	GPL
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	xfce-dev-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	glib-gettextize 

%description
Scramble is the command find tool used by the Xffm-filemanager to 
encrypt and descrypt files upon user request. The application is 
also used to schred files before deleting.

%prep
%setup -q

%build
autoreconf -fi -I /usr/share/xfce4/dev-tools/m4macros
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_bindir}/%{name}
%{_bindir}/unscramble
%{_mandir}/man1/*
%{_datadir}/xffm/%{name}
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 4.5.0-8mdv2011.0
+ Revision: 614827
- the mass rebuild of 2010.1 packages

* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 4.5.0-7mdv2010.1
+ Revision: 509815
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 4.5.0-6mdv2009.0
+ Revision: 260571
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.5.0-5mdv2009.0
+ Revision: 252184
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 11 2007 Thierry Vignaud <tv@mandriva.org> 4.5.0-3mdv2008.1
+ Revision: 117273
- rebuild (missing on ia32)


* Wed Mar 07 2007 Nicolas Lécureuil <neoclust@mandriva.org> 4.5.0-2mdv2007.1
+ Revision: 134797
- Fix Group

* Tue Jan 09 2007 Crispin Boylan <crisb@mandriva.org> 4.5.0-1mdv2007.1
+ Revision: 106475
- First mandriva package
- Create scramble

