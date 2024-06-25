class HyprGenOpts:
	sensitivity: float = 1.0
	apply_sens_to_raw: int = 0
	border_size:int = 1
	no_border_on_floating:int = 1
	border_part_of_window:int = 1
    gaps_in:int = 2
    gaps_out: int = 20
    gaps_workspaces:int = 0
    no_focus_fallback: int = 0
    resize_on_border: int = 0
    extend_border_grab_area:int = 15
    hover_icon_on_border:int = 1
    layout:str = "dwindle"
    allow_tearing: int = 1
    resize_corner: int = 0
class HyprMiscOpts:
    disable_hyprland_logo:int = 0
    disable_splash_rendering:int = 0
    #col.splash:int = 0x55ffffff
    splash_font_family:str = ""
    font_family:str = "Sans"
    force_default_wallpaper:int = -1
    vfr:int = 1
    vrr:int = 1
    mouse_move_enables_dpms:int = 0
    key_press_enables_dpms:int = 0
    always_follow_on_dnd: int = 1
    layers_hog_keyboard_focus: int = 1
    animate_manual_resizes: int = 1
    animate_mouse_windowdragging: int = 1
    disable_autoreload: int = 0
    enable_swallow: int = 0
    swallow_regex:str = ""
    swallow_exception_regex:str = ""
    focus_on_activate: int = 0
    no_direct_scanout:int = 1
    mouse_move_focuses_monitor:int = 1
    render_ahead_of_time: int = 0
    render_ahead_safezone:int = 1
    allow_session_lock_restore: int = 0
    close_special_on_empty:int = 1
    background_color: int = 0xff111111
    new_window_takes_over_fullscreen: int = 0
    initial_workspace_tracking:int = 1
    middle_click_paste:int = 1

class HyprGroupOpts:
	insert_after_current:int = 1
    focus_removed_window:int = 1
class Hypr_groupbar_Opts:
    enabled:int = 1
    font_family:str = ""
    font_size:int = 8
    gradients:int = 1
    height:int = 14
    priority:int = 3
    render_titles:int = 1
    scrolling:int = 1
    text_color:int = 0xffffffff
    stacked: int = 0

class HyprDebugOpts:
	int: int = 0
    log_damage: int = 0
    overlay: int = 0
    damage_blink: int = 0
    disable_logs:int = 1
    disable_time:int = 1
    enable_stdout_logs: int = 0
    damage_tracking: int = 0
    manual_crash: int = 0
    suppress_errors: int = 0
    error_limit:int = 5
    error_position: int = 0
    watchdog_timeout:int = 5
    disable_scale_checks: int = 0
    colored_stdout_logs:int = 1

class HyprDecorationOpts:
    rounding: int = 0
    blur__enabled:int = 1
    blur__size:int = 8
    blur__passes:int = 1
    blur__ignore_opacity: int = 0
    blur__new_optimizations:int = 1
    blur__xray: int = 0
    blur__contrast: float = 0.8916
    blur__brightness:float = 1.0
    blur__vibrancy: float = 0.1696
    blur__vibrancy_darkness: float = 0.0
    blur__noise: float = 0.0117
    blur__special: int = 0
    blur__popups: int = 0
    blur__popups_ignorealpha:float = 0.2
    active_opacity:float = 1.0
    inactive_opacity:float = 1.0
    fullscreen_opacity:float = 1.0
    no_blur_on_oversized: int = 0
    drop_shadow:int = 1
    shadow_range:int = 4
    shadow_render_power:int = 3
    shadow_ignore_window:int = 1
    shadow_offset: tuple = (0,0)
    shadow_scale:float = 1.0
    col__shadow:int = 0xee1a1a1a
    col__shadow_inactive: int = 1
    dim_inactive: int = 0
    dim_strength:float = 0.5
    dim_special: float = 0.2
    dim_around: float = 0.4
    screen_shader:str = ""


class HyprDwindleOpts:
	pseudotile: int = 0
    force_split: int = 0
    permanent_direction_override: int = 0
    preserve_split: int = 0
    special_scale_factor: float = 1.0
    split_width_multiplier: float = 1.0
    no_gaps_when_only: int = 0
    use_active_for_splits:int = 1
    default_split_ratio: float = 1.0
    smart_split: int = 0
    smart_resizing:int = 1

class HyprMasterOpts:
    special_scale_factor: float = 1.0
    mfact: float = 0.55
    new_status: str = "slave"
    always_center_master: int = 0
    new_on_active: str = "none"
    new_on_top: int = 0
    no_gaps_when_only: int = 0
    orientation: str =  "left"
    inherit_fullscreen:int = 1
    allow_small_split: int = 0
    smart_resizing:int = 1
    drop_at_cursor:int = 1

class HyprAnimationsOpts:
	enabled:int = 1
    first_launch_animation:int = 1

class HyprInputOpts:
    follow_mouse:int = 1
    mouse_refocus:int = 1
    special_fallthrough: int = 0
    off_window_axis_events:int = 1
    sensitivity:float = 0.0
    accel_profile:str = """
    kb_file:str = """
    kb_layout:str = "us"
    kb_variant:str = ""
    kb_options:str = ""
    kb_rules:str = ""
    kb_model:str = ""
    repeat_rate: int = 25
    repeat_delay: int = 600
    natural_scroll: int = 0
    numlock_by_default: int = 0
    resolve_binds_by_sym: int = 0
    force_no_accel: int = 0
    float_switch_override_focus:int = 1
    left_handed: int = 0
    scroll_method:str = ""
    scroll_button: int = 0
    scroll_button_lock: int = 0
    scroll_factor:float = 1.0
    scroll_points:str = ""
    touchpad__natural_scroll: int = 0
    touchpad__disable_while_typing:int = 1
    touchpad__clickfinger_behavior: int = 0
    touchpad__tap_button_map:str = ""
    touchpad__middle_button_emulation: int = 0
    touchpad__tap_to_click:int = 1
    touchpad__tap_and_drag:int = 1
    touchpad__drag_lock: int = 0
    touchpad__scroll_factor:float = 1.0
    touchdevice__transform: int = 0
    # touchdevice__output", {"[[Auto]]"});
    touchdevice__enabled:int = 1
    tablet__transform: int = 0
    tablet__output:str = ""
    tablet__region_position:tuple = (0,0)
    tablet__region_size:tuple = (0,0)
    tablet__relative_input: int = 0
    tablet__left_handed: int = 0
    tablet__active_area_position:tuple = (0,0)
    tablet__active_area_size:tuple = (0,0)

class HyprBindsOpts:
	pass_mouse_when_bound: int = 0
    scroll_event_delay: int = 300
    workspace_back_and_forth: int = 0
    allow_workspace_cycles: int = 0
    workspace_center_on:int = 1
    focus_preferred_method: int = 0
    ignore_group_lock: int = 0
    movefocus_cycles_fullscreen:int = 1
    disable_keybind_grabbing: int = 0
    window_direction_monitor_fallback:int = 1

class HyprGesturesOpts:
    workspace_swipe: int = 0
    workspace_swipe_fingers: int = 3
    workspace_swipe_min_fingers: int = 0
    workspace_swipe_distance: int = 300
    workspace_swipe_invert:int = 1
    workspace_swipe_min_speed_to_force", Hyprlang::INT{30});
    workspace_swipe_cancel_ratio", {0.5f});
    workspace_swipe_create_new:int = 1
    workspace_swipe_direction_lock:int = 1
    workspace_swipe_direction_lock_threshold", Hyprlang::INT{10});
    workspace_swipe_forever: int = 0
    workspace_swipe_use_r: int = 0
    workspace_swipe_touch: int = 0

    class HyprXOpts:
	"xwayland:use_nearest_neighbor:int = 1
    "xwayland:force_zero_scaling: int = 0

class Hypr_opengl_Opts:
    "opengl:nvidia_anti_flicker:int = 1
    "opengl:force_introspection", Hyprlang::INT{2});

    "cursor:no_hardware_cursors: int = 0
    "cursor:no_break_fs_vrr: int = 0
    "cursor:min_refresh_rate", Hyprlang::INT{24});
    "cursor:hotspot_padding:int = 1
    "cursor:inactive_timeout: int = 0
    "cursor:no_warps: int = 0
    "cursor:persistent_warps: int = 0
    "cursor:warp_on_change_workspace: int = 0
    "cursor:default_monitor:str = """
    "cursor:zoom_factor", {1.f});
    "cursor:zoom_rigid: int = 0
    "cursor:enable_hyprcursor:int = 1
    "cursor:hide_on_key_press: int = 0
    "cursor:hide_on_touch:int = 1

    # "autogenerated: int = 0
	#
    # "general:col.active_border", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0xffffffff"});
    # "general:col.inactive_border", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0xff444444"});
    # "general:col.nogroup_border", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0xffffaaff"});
    # "general:col.nogroup_border_active", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0xffff00ff"});
	#
    # "group:col.border_active", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66ffff00"});
    # "group:col.border_inactive", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66777700"});
    # "group:col.border_locked_active", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66ff5500"});
    # "group:col.border_locked_inactive", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66775500"});
	#
    # "group:groupbar:col.active", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66ffff00"});
    # "group:groupbar:col.inactive", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66777700"});
    # "group:groupbar:col.locked_active", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66ff5500"});
    # "group:groupbar:col.locked_inactive", Hyprlang::CConfigCustomValueType{&configHandleGradientSet, configHandleGradientDestroy, "0x66775500"});
	#
    # // devices
    # m_pConfig->addSpecialCategory("device", {"name"});
    # m_pConfig->addSpecialConfigValue("device", "sensitivity", {0.F});
    # m_pConfig->addSpecialConfigValue("device", "accel_profile:str = ""
    # m_pConfig->addSpecialConfigValue("device", "kb_file:str = ""
    # m_pConfig->addSpecialConfigValue("device", "kb_layout", {"us"});
    # m_pConfig->addSpecialConfigValue("device", "kb_variant:str = ""
    # m_pConfig->addSpecialConfigValue("device", "kb_options:str = ""
    # m_pConfig->addSpecialConfigValue("device", "kb_rules:str = ""
    # m_pConfig->addSpecialConfigValue("device", "kb_model:str = ""
    # m_pConfig->addSpecialConfigValue("device", "repeat_rate", Hyprlang::INT{25});
    # m_pConfig->addSpecialConfigValue("device", "repeat_delay", Hyprlang::INT{600});
    # m_pConfig->addSpecialConfigValue("device", "natural_scroll: int = 0
    # m_pConfig->addSpecialConfigValue("device", "tap_button_map:str = ""
    # m_pConfig->addSpecialConfigValue("device", "numlock_by_default: int = 0
    # m_pConfig->addSpecialConfigValue("device", "resolve_binds_by_sym: int = 0
    # m_pConfig->addSpecialConfigValue("device", "disable_while_typing:int = 1
    # m_pConfig->addSpecialConfigValue("device", "clickfinger_behavior: int = 0
    # m_pConfig->addSpecialConfigValue("device", "middle_button_emulation: int = 0
    # m_pConfig->addSpecialConfigValue("device", "tap-to-click:int = 1
    # m_pConfig->addSpecialConfigValue("device", "tap-and-drag:int = 1
    # m_pConfig->addSpecialConfigValue("device", "drag_lock: int = 0
    # m_pConfig->addSpecialConfigValue("device", "left_handed: int = 0
    # m_pConfig->addSpecialConfigValue("device", "scroll_method:str = ""
    # m_pConfig->addSpecialConfigValue("device", "scroll_button: int = 0
    # m_pConfig->addSpecialConfigValue("device", "scroll_button_lock: int = 0
    # m_pConfig->addSpecialConfigValue("device", "scroll_points:str = ""
    # m_pConfig->addSpecialConfigValue("device", "transform: int = 0
    # m_pConfig->addSpecialConfigValue("device", "output:str = ""
    # m_pConfig->addSpecialConfigValue("device", "enabled:int = 1                  //
    # only
    # for mice, touchpads, and touchdevices
    # m_pConfig->addSpecialConfigValue("device", "region_position", Hyprlang::VEC2{0, 0});      // only for tablets
    # m_pConfig->addSpecialConfigValue("device", "region_size", Hyprlang::VEC2{0, 0});          // only for tablets
    # m_pConfig->addSpecialConfigValue("device", "relative_input: int = 0           // 
    # only 
    # for tablets
    # m_pConfig->addSpecialConfigValue("device", "active_area_position", Hyprlang::VEC2{0, 0}); // only for tablets
    # m_pConfig->addSpecialConfigValue("device", "active_area_size", Hyprlang::VEC2{0, 0});     // only for tablets
	#
    # // keywords
    # m_pConfig->registerHandler(&::handleRawExec, "exec", {false});
    # m_pConfig->registerHandler(&::handleExecOnce, "exec-once", {false});
    # m_pConfig->registerHandler(&::handleMonitor, "monitor", {false});
    # m_pConfig->registerHandler(&::handleBind, "bind", {true});
    # m_pConfig->registerHandler(&::handleUnbind, "unbind", {false});
    # m_pConfig->registerHandler(&::handleWorkspaceRules, "workspace", {false});
    # m_pConfig->registerHandler(&::handleWindowRule, "windowrule", {false});
    # m_pConfig->registerHandler(&::handleLayerRule, "layerrule", {false});
    # m_pConfig->registerHandler(&::handleWindowRuleV2, "windowrulev2", {false});
    # m_pConfig->registerHandler(&::handleBezier, "bezier", {false});
    # m_pConfig->registerHandler(&::handleAnimation, "animation", {false});
    # m_pConfig->registerHandler(&::handleSource, "source", {false});
    # m_pConfig->registerHandler(&::handleSubmap, "submap", {false});
    # m_pConfig->registerHandler(&::handleBlurLS, "blurls", {false});
    # m_pConfig->registerHandler(&::handlePlugin, "plugin", {false});
    # m_pConfig->registerHandler(&::handleEnv, "env", {true});
