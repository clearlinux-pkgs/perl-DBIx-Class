#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-Class
Version  : 0.082842
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-0.082842.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/DBIx-Class-0.082842.tar.gz
Summary  : 'Extensible and flexible object <-> relational mapper.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-DBIx-Class-bin = %{version}-%{release}
Requires: perl-DBIx-Class-license = %{version}-%{release}
Requires: perl-DBIx-Class-man = %{version}-%{release}
Requires: perl-DBIx-Class-perl = %{version}-%{release}
Requires: perl(JSON::Any)
Requires: perl(MooseX::Types)
Requires: perl(MooseX::Types::JSON)
Requires: perl(MooseX::Types::LoadableClass)
Requires: perl(MooseX::Types::Path::Class)
Requires: perl(SQL::Abstract::Util)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Grouped)
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Config::Any)
BuildRequires : perl(Context::Preserve)
BuildRequires : perl(DBD::SQLite)
BuildRequires : perl(DBI)
BuildRequires : perl(Data::Dumper::Concise)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Hash::Merge)
BuildRequires : perl(JSON::Any)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Find)
BuildRequires : perl(Moo)
BuildRequires : perl(MooseX::Types)
BuildRequires : perl(MooseX::Types::JSON)
BuildRequires : perl(MooseX::Types::LoadableClass)
BuildRequires : perl(MooseX::Types::Path::Class)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Path::Class)
BuildRequires : perl(SQL::Abstract::Classic)
BuildRequires : perl(Scope::Guard)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Warn)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::clean)
BuildRequires : perl-Class-C3-Componentised
BuildRequires : perl-DBD-SQLite

%description
See AUTHORS and LICENSE included with this distribution. All rights reserved.
NAME
DBIx::Class - Extensible and flexible object <-> relational mapper.

%package bin
Summary: bin components for the perl-DBIx-Class package.
Group: Binaries
Requires: perl-DBIx-Class-license = %{version}-%{release}

%description bin
bin components for the perl-DBIx-Class package.


%package dev
Summary: dev components for the perl-DBIx-Class package.
Group: Development
Requires: perl-DBIx-Class-bin = %{version}-%{release}
Provides: perl-DBIx-Class-devel = %{version}-%{release}
Requires: perl-DBIx-Class = %{version}-%{release}

%description dev
dev components for the perl-DBIx-Class package.


%package license
Summary: license components for the perl-DBIx-Class package.
Group: Default

%description license
license components for the perl-DBIx-Class package.


%package man
Summary: man components for the perl-DBIx-Class package.
Group: Default

%description man
man components for the perl-DBIx-Class package.


%package perl
Summary: perl components for the perl-DBIx-Class package.
Group: Default
Requires: perl-DBIx-Class = %{version}-%{release}

%description perl
perl components for the perl-DBIx-Class package.


%prep
%setup -q -n DBIx-Class-0.082842
cd %{_builddir}/DBIx-Class-0.082842

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-Class
cp %{_builddir}/DBIx-Class-0.082842/LICENSE %{buildroot}/usr/share/package-licenses/perl-DBIx-Class/9a1990499bf1c624338a96288466ea679b285b34
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dbicadmin

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Class.3
/usr/share/man/man3/DBIx::Class::AccessorGroup.3
/usr/share/man/man3/DBIx::Class::Admin.3
/usr/share/man/man3/DBIx::Class::CDBICompat.3
/usr/share/man/man3/DBIx::Class::CDBICompat::AbstractSearch.3
/usr/share/man/man3/DBIx::Class::CDBICompat::ColumnsAsHash.3
/usr/share/man/man3/DBIx::Class::CDBICompat::Copy.3
/usr/share/man/man3/DBIx::Class::CDBICompat::Iterator.3
/usr/share/man/man3/DBIx::Class::CDBICompat::NoObjectIndex.3
/usr/share/man/man3/DBIx::Class::CDBICompat::Relationship.3
/usr/share/man/man3/DBIx::Class::CDBICompat::Relationships.3
/usr/share/man/man3/DBIx::Class::CDBICompat::SQLTransformer.3
/usr/share/man/man3/DBIx::Class::Carp.3
/usr/share/man/man3/DBIx::Class::Core.3
/usr/share/man/man3/DBIx::Class::Cursor.3
/usr/share/man/man3/DBIx::Class::DB.3
/usr/share/man/man3/DBIx::Class::Exception.3
/usr/share/man/man3/DBIx::Class::FilterColumn.3
/usr/share/man/man3/DBIx::Class::InflateColumn.3
/usr/share/man/man3/DBIx::Class::InflateColumn::DateTime.3
/usr/share/man/man3/DBIx::Class::InflateColumn::File.3
/usr/share/man/man3/DBIx::Class::Manual.3
/usr/share/man/man3/DBIx::Class::Manual::Component.3
/usr/share/man/man3/DBIx::Class::Manual::Cookbook.3
/usr/share/man/man3/DBIx::Class::Manual::DocMap.3
/usr/share/man/man3/DBIx::Class::Manual::Example.3
/usr/share/man/man3/DBIx::Class::Manual::FAQ.3
/usr/share/man/man3/DBIx::Class::Manual::Features.3
/usr/share/man/man3/DBIx::Class::Manual::Glossary.3
/usr/share/man/man3/DBIx::Class::Manual::Intro.3
/usr/share/man/man3/DBIx::Class::Manual::Joining.3
/usr/share/man/man3/DBIx::Class::Manual::QuickStart.3
/usr/share/man/man3/DBIx::Class::Manual::Reading.3
/usr/share/man/man3/DBIx::Class::Manual::ResultClass.3
/usr/share/man/man3/DBIx::Class::Manual::Troubleshooting.3
/usr/share/man/man3/DBIx::Class::Optional::Dependencies.3
/usr/share/man/man3/DBIx::Class::Ordered.3
/usr/share/man/man3/DBIx::Class::PK.3
/usr/share/man/man3/DBIx::Class::PK::Auto.3
/usr/share/man/man3/DBIx::Class::PK::Auto::DB2.3
/usr/share/man/man3/DBIx::Class::PK::Auto::MSSQL.3
/usr/share/man/man3/DBIx::Class::PK::Auto::MySQL.3
/usr/share/man/man3/DBIx::Class::PK::Auto::Oracle.3
/usr/share/man/man3/DBIx::Class::PK::Auto::Pg.3
/usr/share/man/man3/DBIx::Class::PK::Auto::SQLite.3
/usr/share/man/man3/DBIx::Class::Relationship.3
/usr/share/man/man3/DBIx::Class::Relationship::Base.3
/usr/share/man/man3/DBIx::Class::ResultClass::HashRefInflator.3
/usr/share/man/man3/DBIx::Class::ResultSet.3
/usr/share/man/man3/DBIx::Class::ResultSet::Pager.3
/usr/share/man/man3/DBIx::Class::ResultSetColumn.3
/usr/share/man/man3/DBIx::Class::ResultSetManager.3
/usr/share/man/man3/DBIx::Class::ResultSource.3
/usr/share/man/man3/DBIx::Class::ResultSource::Table.3
/usr/share/man/man3/DBIx::Class::ResultSource::View.3
/usr/share/man/man3/DBIx::Class::ResultSourceHandle.3
/usr/share/man/man3/DBIx::Class::ResultSourceProxy::Table.3
/usr/share/man/man3/DBIx::Class::Row.3
/usr/share/man/man3/DBIx::Class::SQLMaker.3
/usr/share/man/man3/DBIx::Class::SQLMaker::ClassicExtensions.3
/usr/share/man/man3/DBIx::Class::SQLMaker::LimitDialects.3
/usr/share/man/man3/DBIx::Class::SQLMaker::OracleJoins.3
/usr/share/man/man3/DBIx::Class::Schema.3
/usr/share/man/man3/DBIx::Class::Schema::Versioned.3
/usr/share/man/man3/DBIx::Class::Serialize::Storable.3
/usr/share/man/man3/DBIx::Class::StartupCheck.3
/usr/share/man/man3/DBIx::Class::Storage.3
/usr/share/man/man3/DBIx::Class::Storage::BlockRunner.3
/usr/share/man/man3/DBIx::Class::Storage::DBI.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ACCESS.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ADO.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ADO::MS_Jet.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ADO::MS_Jet::Cursor.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ADO::Microsoft_SQL_Server.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ADO::Microsoft_SQL_Server::Cursor.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::AutoCast.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Cursor.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::DB2.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Firebird.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Firebird::Common.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::IdentityInsert.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Informix.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::InterBase.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::MSSQL.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::NoBindVars.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC::ACCESS.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC::DB2_400_SQL.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC::Firebird.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC::Microsoft_SQL_Server.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::ODBC::SQL_Anywhere.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Oracle.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Oracle::Generic.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Oracle::WhereJoins.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Pg.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Balancer.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Balancer::First.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Balancer::Random.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Introduction.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Pool.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::Replicant.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Replicated::WithDSN.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::SQLAnywhere.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::SQLAnywhere::Cursor.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::SQLite.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::ASE.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::ASE::NoBindVars.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::FreeTDS.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::MSSQL.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::Microsoft_SQL_Server.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::Sybase::Microsoft_SQL_Server::NoBindVars.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::UniqueIdentifier.3
/usr/share/man/man3/DBIx::Class::Storage::DBI::mysql.3
/usr/share/man/man3/DBIx::Class::Storage::Debug::PrettyTrace.3
/usr/share/man/man3/DBIx::Class::Storage::Statistics.3
/usr/share/man/man3/DBIx::Class::Storage::TxnScopeGuard.3
/usr/share/man/man3/DBIx::Class::UTF8Columns.3
/usr/share/man/man3/SQL::Translator::Parser::DBIx::Class.3
/usr/share/man/man3/SQL::Translator::Producer::DBIx::Class::File.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-Class/9a1990499bf1c624338a96288466ea679b285b34

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dbicadmin.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/AccessorGroup.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Admin.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Admin/Descriptive.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Admin/Types.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Admin/Usage.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/AbstractSearch.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/AccessorMapping.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/AttributeAPI.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/AutoUpdate.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/ColumnCase.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/ColumnGroups.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/ColumnsAsHash.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Constraints.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Constructor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Copy.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/DestroyWarning.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/GetSet.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/ImaDBI.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Iterator.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/LazyLoading.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/LiveObjectIndex.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/NoObjectIndex.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Pager.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/ReadOnly.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Relationship.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Relationships.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Retrieve.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/SQLTransformer.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Stringify.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/TempColumns.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/CDBICompat/Triggers.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Carp.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ClassResolver/PassThrough.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Componentised.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Core.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Cursor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/DB.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Exception.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/FilterColumn.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/FilterColumn.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/InflateColumn.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/InflateColumn.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/InflateColumn/DateTime.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/InflateColumn/DateTime.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/InflateColumn/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Component.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/DocMap.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Example.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/FAQ.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Features.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Glossary.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Intro.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Joining.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/QuickStart.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Reading.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/ResultClass.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Manual/Troubleshooting.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Optional/Dependencies.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Optional/Dependencies.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Ordered.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/DB2.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/MSSQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/MySQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/Oracle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/Pg.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/PK/Auto/SQLite.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/Accessor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/Base.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/BelongsTo.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/CascadeActions.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/HasMany.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/HasOne.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/Helpers.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/ManyToMany.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Relationship/ProxyMethods.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultClass/HashRefInflator.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSet.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSet/Pager.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSetColumn.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSetManager.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSetProxy.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/RowParser.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/RowParser/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/Table.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/Table.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/View.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSource/View.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSourceHandle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSourceProxy.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSourceProxy/Table.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/ResultSourceProxy/Table.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Row.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks/MSSQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks/MySQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks/Oracle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks/OracleJoins.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLAHacks/SQLite.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/ACCESS.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/ClassicExtensions.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/LimitDialects.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/MSSQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/MySQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/Oracle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/OracleJoins.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/SQLMaker/SQLite.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Schema.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Schema/Versioned.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Serialize/Storable.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/StartupCheck.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/BlockRunner.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ACCESS.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO/CursorUtils.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO/MS_Jet.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO/MS_Jet/Cursor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO/Microsoft_SQL_Server.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ADO/Microsoft_SQL_Server/Cursor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/AutoCast.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Cursor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/DB2.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Firebird.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Firebird/Common.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/IdentityInsert.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Informix.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/InterBase.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/MSSQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/NoBindVars.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC/ACCESS.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC/DB2_400_SQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC/Firebird.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC/Microsoft_SQL_Server.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/ODBC/SQL_Anywhere.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Oracle.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Oracle/Generic.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Oracle/WhereJoins.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Pg.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Balancer.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Balancer/First.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Balancer/Random.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Introduction.pod
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Pool.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Replicant.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/Types.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Replicated/WithDSN.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/SQLAnywhere.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/SQLAnywhere/Cursor.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/SQLite.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/ASE.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/ASE/NoBindVars.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/FreeTDS.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/MSSQL.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/Microsoft_SQL_Server.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/Sybase/Microsoft_SQL_Server/NoBindVars.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/UniqueIdentifier.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBI/mysql.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/DBIHacks.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/Debug/PrettyTrace.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/Statistics.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/Storage/TxnScopeGuard.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/UTF8Columns.pm
/usr/lib/perl5/vendor_perl/5.34.0/DBIx/Class/_Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/SQL/Translator/Parser/DBIx/Class.pm
/usr/lib/perl5/vendor_perl/5.34.0/SQL/Translator/Producer/DBIx/Class/File.pm
