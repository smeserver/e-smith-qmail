Summary: startup scripts for Dan Bernstein's qmail package
%define name e-smith-qmail
Name: %{name}
%define version 1.10.0
%define release 13
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-qmail-1.10.0.no_connect_zero.patch
Patch1: e-smith-qmail-1.10.0-update-groups.patch
Patch2: e-smith-qmail-1.10.0-DomainMailOnly.patch
Patch3: e-smith-qmail-1.10.0-MailRouting.patch 
Patch4: e-smith-qmail-1.10.0-MaxMessageSize.patch
Patch5: e-smith-qmail-1.10.0-helohost.patch
Patch6: e-smith-qmail-1.10.0-ExcludeFromEveryoneEmail.patch
Patch7: e-smith-qmail-1.10.0-forcejunkmaildir.patch
Patch8: e-smith-qmail-1.10.0-qmailadmin.patch
Patch9: e-smith-qmail-1.10.0-sv.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools >= 1.13.0-04
BuildArchitectures: noarch
Requires: qmail
Requires: dot-forward
Requires: fastforward
Requires: runit
Requires: e-smith-email
Requires: qmail-workaround
Provides: e-smith-mta
Conflicts: runit < 1.7
Obsoletes: qmail-initscripts
AutoReqProv: no

%changelog
* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 1.10.0-13
- Change ownership/perms on /var/qmail/alias directory [SME: 2709]

* Thu Feb 15 2007 Charlie Brady <charlie_brady@mitel.com>
- Use sv rather than deprecated runsvctrl in ip-up script. [SME: 2486]

* Mon Jan 22 2007 Shad L. Lords <slords@mail.com> 1.10.0-11
- Allow admin user to be configured via users panel. [SME: 827]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Aug 25 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-10
- Force creation of junkmail folder as some users like to delete
  it [SME: 1130]

* Mon Aug 14 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-09
- Allow optional EveryoneEmail property of user and 'admin' accounts
  If set to 'no', do not include this user in the shared/everyone
  email alias [SME: 1842]

* Thu Aug 3 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-08
- Allow optional $smtpd{HeloHost} value for configuring HELO host,
  defaulting to $DomainName [SME: 1790]

* Thu Jun 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-07
- Default qmail{MaxMessageSize} to 15,000,000 bytes [SME: 1624]

* Mon May 15 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-06
- Bump version only [SME: 1415]

* Wed May 10 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-05sme01
- Allow optional MailServer property of domains db records and
  deliver mail in this order of preference:
  - As per the MailServer property of the domain
  - $DelegateMailServer 
  - localhost (i.e. locally)
  NOTE: 
  - If DelegateMailServer is not set, the users must exist on the
    gateway or mail will be rejected
  - If DelegateMailServer is set, all mail for the domain will be
    forwarded to the relevant internal mail server [SME: 1253]

* Wed May 10 2006 Gordon Rowell <gordonr@gormand.com.au> 1.10.0-04sme01
- Remove virtualdomains entries for hosts db entries. We only
  handle mail for domains without customisation [SME: 1415]

* Sat Apr  8 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-03
- Update group .qmail files when deleting/modifying users. [SME: 1200]

* Thu Mar 23 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-02
- Use shared library to block 0.0.0.0 MX mail loops. [SME: 1116]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.10.0-01
- Roll stable stream version. [SME: 1016]

* Fri Mar 03 2006 Charlie Brady <charlie_brady@mitel.com> 1.9.1-05
- Add ~alias/.qmail-shared-default symlink. [SME: 764]

* Thu Feb 16 2006 Charlie Brady <charlieb@e-smith.com> 1.9.1-04
- Fix migration when AdminEmail is not set. [SME: 818]

* Thu Feb 16 2006 Charlie Brady <charlieb@e-smith.com> 1.9.1-03
- Use standard user .qmail template for admin user. Migrate
  AdminEmail setting to $admin{ForwardAddress}. [SME: 818]

* Tue Jan 24 2006 Charlie Brady <charlieb@e-smith.com> 1.9.1-02
- Fix duplicate symlink creation attempt in bootstrap-console-save
  directory (during RPM build). [SME: 555]

* Wed Jan 11 2006 Gordon Rowell <gordonr@gormand.com.au> 1.9.1-01
- Roll patches to 1.9.0-16
- Change ~alias/.qmail{default,localdelivery-default,shared} into
  directory templates [SME: 440]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.9.0-16
- Bump release number only

* Tue Nov 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-15]
- Fix broken symlink in group-delete event. Delete -default .qmail file
  when deleting group. [SF: 1363973]

* Tue Nov  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-14]
- Improve /var/qmail/users/assign/70pseudonyms error handling. [SF: 1337029]
- Fix error text from 60users template fragment. [SF: 1345206]

* Fri Oct 21 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-13]
- Add quotes around 'Recipient unknown' when calling bouncesaying.
  Otherwise we're trying to call a program called 'unknown' [SF: 1334002]

* Wed Oct 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-12]
- Ensure failsafe .qmail file if EmailForward property is not set.
  [SF: 1330452]

* Fri Oct  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-11]
- Expand virtualdomains in pseudonym-* events. Replace use of control/1
  by generic actions, plus qmail-newu symlinked into event directories.
  [SF: 1311349]

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.9.0-10]
- Split up templates-user/.qmail into fragments which return 
  one or zero lines. It's much cleaner and helps with add-ons.
  Move .qmail/20Forward -> 70Forward to leave more room for
  add-ons [SF: 1252336]
- Minor fixups - thanks Stephen Noble [SF: 1252336]
- TODO: Remove the 10Filter stuff and migrate 
  qmail{DeliveryInstruction} and qmail{DeliveryType} 

* Mon Sep 19 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-09]
- Correct /var/qmail/users/assign/50system fragment so that
  mail for system accounts is delivered to admin [SF: 1284311]

* Tue Sep 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.9.0-08]
- Add extension address handling for pseudonyms and groups.
  [SF: 1286823]

* Mon Aug 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-07]
- Make correct /service symlink, so that a runit finds the
  run files. [SF: 1264668]

* Wed Aug 10 2005 Shad Lords <slords@mail.com>
- [1.9.0-06]
- Add empty template-begin header for users/assign
- Add requires for e-smith-email
- Add provides e-smith-mta

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-05]
- Add in all qmail specific code from e-smith-email. [SF: 1255261]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Remove dangling conf-migrate-* symlink [charlieb MN00062545]

* Tue Dec 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Remove no longer needed conf-migrate-* action [charlieb MN00062545]
- Replace deprecated Copyright header with License header.

* Thu Feb 12 2004 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-02]
- Updating with esmith::Build::CreateLinks, and the new genfilelist options.
- Yanked migrate-qmail-logfiles, as it was causing problems.
  [msoulier dpar-20522]

* Fri Feb  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-01]
- rolling to dev - 1.9.0

* Thu Aug 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-02]
- Adding K* init symlinks in runlevels 0, 1 and 6. [msoulier 9761]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Changing version to stable stream number - 1.8.0

* Wed Nov  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Rolling development stream version to 1.7.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Roll to maintained version number to 1.6.0

* Wed Aug 21 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Remove bogus e-smith-base dependency, which shows as an unmet
  dependency on our workstations.
- Add rc7.d symlink [charlieb 4458]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Changing version to development stream number to 1.5.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Changing version to maintained stream number to 1.4.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.9-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.8-01]
- testing co2rpm --force

* Thu May 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.7-01]
- Remove world read and execute permission from qmail log directory.

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.6-01]
- /supervise/qmail -> /service/qmail  [gordonr 3044]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.5-01]
- Added /bin, /usr/bin and /usr/local/bin to qmail's path [gordonr 3044]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.4-01]
- And create /var/log/qmail [gordonr 3044]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.3-01]
- And create directory for pipes to be written to [gordonr 3044]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.2-01]
- Created pipes, symlinks and empty files in SPEC file [gordonr 3044]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.1-01]
- Initial CVS import

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- rollRPM: Rolled version number to 1.3.0-01. Includes patches up to 1.2.0-02.

* Fri Aug 17 2001 gordonr
- [1.2.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-04.

* Tue May 1 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-04]
- added /var/log/qmail to filelist

* Tue May 1 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-03]
- added migrate-qmail-logfiles action to post-upgrade

* Mon Apr 30 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-02]
- added conf-migrate-qmail-variables actions to migrate qmail.init
  configuration variable to qmail
- added e-smith header to files

* Mon Apr 30 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-01]
- initial release

%description
Startup scripts for Dan Bernstein's qmail package.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
perl createlinks

mkdir -p root/service
ln -s ../var/service/qmail root/service/qmail
mkdir -p root/var/service/qmail/supervise
touch root/var/service/qmail/down
mkdir -p root/var/service/qmail/log/supervise
mkdir -p root/var/log/qmail

mkdir -p root/etc/e-smith/templates/var/qmail/users/assign
touch root/etc/e-smith/templates/var/qmail/users/assign/template-begin

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir '/var/service/qmail' 'attr(1755,root,root)' \
    --file '/var/service/qmail/down' 'attr(0644,root,root)' \
    --file '/var/service/qmail/run' 'attr(0755,root,root)' \
    --file '/var/service/qmail/control/1' 'attr(0750,root,root)' \
    --dir '/var/service/qmail/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/qmail/log' 'attr(0755,root,root)' \
    --file '/var/service/qmail/log/run' 'attr(0755,root,root)' \
    --dir '/var/service/qmail/log/supervise' 'attr(0700,root,root)' \
    --dir '/var/log/qmail' 'attr(2750,qmaill,nofiles)' \
    --dir '/var/qmail/alias' 'attr(2755,alias,qmail)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
