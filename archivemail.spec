Summary:	Archive and compress old email
Summary(pl.UTF-8):	Archiwizowanie starej poczty
Name:		archivemail
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/archivemail/%{name}-%{version}.tar.gz
# Source0-md5:	e444424688e6ec063e829176e4eb62e2
Patch0:		%{name}-invalid-message.patch
URL:		http://archivemail.sourceforge.net/
BuildRequires:	python-devel >= 2.0
%pyrequires_eq	python
# for warnings.py
Requires:	python-modules
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

%description -l pl.UTF-8
Archivemail jest, napisanym w języku Python, narzędziem służącym
archiwizowaniu i kompresowaniu starej poczty.

Za pomocą programu można przenosić wiadomości starsze niż określona
liczba dni do oddzielnej skrzynki w formacie mbox, która jest
kompresowana przy użyciu programu 'gzip'.

Przykładowo, ktoś jest od 6 lat zapisany na listę 'linux-kernel' i
jego skrzynka zajmuje już ponad 160MB, a jej otwarcie trwa trochę
czasu. Archivemail może przenieść wszystkie wiadomości, powiedzmy
sprzed 6 miesięcy, do oddzielnej, skompresowanej skrzynki, zostawiając
tylko najnowsze listy.

Archivemail potrafi zapisywać i odczytywać następujące formaty
skrzynek pocztowych: IMAP, Maildir, MH oraz mbox.

%prep
%setup -q
%patch0 -p3

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
