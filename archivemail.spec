

Summary:	Archive and compress old email
Summary(pl):	Archiwizowanie starej poczty
Name:		archivemail
Version:	0.6.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/archivemail/%{name}-%{version}.tar.gz
# Source0-md5:	aaf071effc9576cc14f3b0eee1d2321e
URL:		http://archivemail.sourceforge.net/
BuildRequires:	python-devel >= 2.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archivemail is a tool written in Python for archiving and
compressing old email in mailboxes.

It can move messages older than the specified number of days to a
separate 'archive' mbox-format mailbox that is compressed with 'gzip'.

For example, have you been subscribing to the 'linux-kernel' mailing
list for the last 6 years and ended up with an 160-meg mailbox that
Mutt is taking a long time to load? Archivemail can move all
messages that are older than 6 months to a separate compressed
mailbox, and leave you with just the most recent messages.

It supports IMAP, Maildir, MH and mbox-format mailboxes.

%description -l pl
Archivemail jest, napisanym w jêzyku Python, narzêdziem s³u¿±cym
archiwizowaniu i kompresowaniu starej poczty.

Za pomoc± programu mo¿na przenosiæ wiadomo¶ci starsze ni¿ okre¶lona
liczba dni do oddzielnej skrzynki w formacie mbox, która jest
kompresowana przy u¿yciu programu 'gzip'.

Przyk³adowo, kto¶ jest od 6 lat zapisany na listê 'linux-kernel' i
jego skrzynka zajmuje ju¿ ponad 160MB, a jej otwarcie trwa trochê
czasu. Archivemail mo¿e przenie¶æ wszystkie wiadomo¶ci, powiedzmy
sprzed 6 miesiêcy, do oddzielnej, skompresowanej skrzynki, zostawiaj±c
tylko najnowsze listy.

Archivemail potrafi zapisywaæ i odczytywaæ nastêpuj±ce formaty
skrzynek pocztowych: IMAP, Maildir, MH oraz mbox.

%prep
%setup -q

%build
# Nothing to be done here.
./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_mandir}
./setup.py install \
	--prefix=%{_prefix} \
	--root=${RPM_BUILD_ROOT}

# This one is ugly.
mv ${RPM_BUILD_ROOT}%{_prefix}/man/man1 ${RPM_BUILD_ROOT}%{_mandir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc CHANGELOG FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
