#!/usr/bin/perl

# Title:       lighttpd SA Important SUSE-SU-2014:0474-1
# Description: fixes two vulnerabilities
# Modified:    2014 May 21
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################
use strict;
use warnings;
use SDP::Core;
use SDP::SUSE;

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
"META_CLASS=Security",
"META_CATEGORY=HAE",
"META_COMPONENT=lighttpd",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-04/msg00002.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Lighttpd';
my $MAIN_PACKAGE = 'lighttpd';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2014:0474-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP3) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0 ) {
	%PACKAGES = (
		'lighttpd' => '1.4.20-2.54.1',
		'lighttpd-mod_cml' => '1.4.20-2.54.1',
		'lighttpd-mod_magnet' => '1.4.20-2.54.1',
		'lighttpd-mod_mysql_vhost' => '1.4.20-2.54.1',
		'lighttpd-mod_rrdtool' => '1.4.20-2.54.1',
		'lighttpd-mod_trigger_b4_dl' => '1.4.20-2.54.1',
		'lighttpd-mod_webdav' => '1.4.20-2.54.1',
		);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

