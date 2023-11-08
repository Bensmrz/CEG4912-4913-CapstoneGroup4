import React from "react";
import { StyleSheet, Text, View, Pressable, TouchableOpacity } from "react-native";

export default function MenuItem(props) {
    const { text, icon, onPress } = props;
    return (
        <TouchableOpacity style={styles.menuItem} onPress={onPress}>
            <View style={styles.menuContent}>
                <Text style={styles.menuIcon}>{icon}</Text>
                <Text style={styles.menuText}>{text}</Text>
            </View>
        </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    menuContent: {
        flexDirection: "column",
        alignItems: "center",
    },
    menuItem: {
        flexDirection: "row",
        alignItems: "center",
        margin: 20,
    },
    menuIcon: {
        width: 80,
        height: 80,
        borderWidth: 1,
        borderColor: "black",
        borderRadius: 10,
        padding: 10,
    },
    menuText: {
        fontSize: 16,
    },
});