import React from "react";
import { StyleSheet, View, Text, Pressable } from "react-native";
import MenuItem from "../assets/components/MenuItem";

export default function MainMenu() {
    const handleMenuItemPress = (menuItem) => {
        console.log("menu item " + menuItem + " pressed");
    };

    const handleLogout = () => {
        console.log("Logout successful");
    };

    return (
        <View style={styles.container}>
            {/* Header */}
            <View style={styles.topNav}>
                <Text style={styles.topNavText}>AppIcon</Text>
                <Text style={styles.topNavText}>Main Menu</Text>
            </View>

            {/* Main Content */}
            <View style={styles.content}>
                <View style={styles.menuRow}>
                    <MenuItem
                        text="Conversation History"
                        icon="ConversationHistoryIcon"
                        onPress={() => handleMenuItemPress(1)}
                    />
                    <MenuItem
                        text="Real-time Viewer"
                        icon="Real-timeViewerIcon"
                        onPress={() => handleMenuItemPress(2)}
                    />
                </View>
                <View style={styles.menuRow}>
                    <MenuItem text="Device Settings" icon="DeviceSettingsIcon" onPress={() => handleMenuItemPress(3)} />
                    <MenuItem
                        text="Application Settings"
                        icon="ApplicationSettingsIcon"
                        onPress={() => handleMenuItemPress(4)}
                    />
                </View>
            </View>

            {/* Logout */}
            <Pressable style={styles.logoutButton} onPress={handleLogout}>
                <Text style={styles.logoutText}>Log Out</Text>
                <Text style={styles.logoutText}>LogOutIcon</Text>
            </Pressable>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
    },
    topNav: {
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
        padding: 16,
    },
    appIcon: {
        width: 40,
        height: 40,
    },
    topNavText: {
        fontSize: 18,
    },
    content: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
    },
    menuRow: {
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        flexWrap: "wrap",
        width: "100%",
    },
    logoutButton: {
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "right",
        padding: 16,
    },
    logoutText: {
        fontSize: 18,
        marginRight: 10,
    },
});