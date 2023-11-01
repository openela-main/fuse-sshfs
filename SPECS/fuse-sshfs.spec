%global _hardened_build 1


Name:           fuse-sshfs
Version:        2.8
Release:        5%{?dist}
Summary:        FUSE-Filesystem to access remote filesystems via SSH
Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/libfuse/sshfs
Source0:        https://github.com/libfuse/sshfs/releases/download/sshfs_%{version}/sshfs-%{version}.tar.gz
Source1:        https://github.com/libfuse/sshfs/releases/download/sshfs_%{version}/sshfs-%{version}.tar.gz.asc
Provides:       sshfs = %{version}-%{release}
Requires:       fuse >= 2.2
Requires:	openssh-clients
BuildRequires:  fuse-devel >= 2.2
BuildRequires:  glib2-devel >= 2.0
BuildRequires:	openssh-clients


%description
This is a FUSE-filesystem client based on the SSH File Transfer Protocol.
Since most SSH servers already support this protocol it is very easy to set
up: i.e. on the server side there's nothing to do.  On the client side
mounting the filesystem is as easy as logging into the server with ssh.


%prep
%setup -q -n sshfs-%{version}


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS
%license COPYING
%{_bindir}/sshfs
%{_mandir}/man1/sshfs.1.gz


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.8-1
- Ver. 2.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 14 2014 Peter Lemenkov <lemenkov@gmail.com> - 2.5-1
- Ver. 2.5
- Removed support for building on EPEL 5 (not sure if it was even possible there)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.4-5
- Build with PIE

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.4-1
- Ver. 2.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.3-1
- Ver. 2.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 18 2010 Peter Lemenkov <lemenkov@gmail.com> 2.2-6
- Fix building on EL-6

* Sun Sep 27 2009 Peter Lemenkov <lemenkov@gmail.com> 2.2-5
- No need for versioning in (Build)Requires for openssh-clients

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> 2.2-4
- Rebuilt with new fuse

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  9 2008 Peter Lemenkov <lemenkov@gmail.com> 2.2-1
- Ver. 2.2

* Sun Sep 28 2008 Peter Lemenkov <lemenkov@gmail.com> 2.1-1
- Ver. 2.1

* Mon May 19 2008 Peter Lemenkov <lemenkov@gmail.com> 2.0-1
- Ver. 2.0

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-2
- Rebuild for GCC 4.3

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-2
- Added missing Requires and BuildRequires - openssh-clients >= 4.4

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 1.9-1
- Ver. 1.9
- Added provides: sshfs
- Modified License field according to Fedora policy.

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.7-2
- Rebuild for FC6

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.7-1
- New version
- Rebuild for FC6

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.6-2
- added missing sshnodelay.so

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.6-1
- Version 1.6

* Mon Feb 13 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.4-2
- small cosmetic fixes

* Mon Feb 13 2006 Peter Lemenkov <lemenkov@newmail.ru> - 1.4-1
- Version 1.4

* Wed Nov 23 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-3
- Use dist

* Fri Nov 04 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-2
- Update deps

* Fri Oct 28 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.2-1
- Initial RPM release.
