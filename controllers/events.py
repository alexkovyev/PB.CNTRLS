from pydispatch import Dispatcher


class ControllersEvents(Dispatcher):
    """
    Dispatcher for controller event handlers. DON'T CREATE instances of this class, use
    cntrls_events.
    """
    _events_ = ['qr_scanned', 'hardware_status_changed']

    def qr_scanned(self, _guid):
        self.emit('qr_scanned', guid=_guid)

    def hardware_status_changed(self, _unit_name, _status):
        self.emit('hardware_status_changed', unit_name=_unit_name, status=_status)


cntrls_events = ControllersEvents()
